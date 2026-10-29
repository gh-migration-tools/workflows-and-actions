#!/usr/bin/env python3
"""Dispatches a workflow_dispatch run and polls it until completion.

Refreshes its GitHub App token along the way so runs that outlive one token's 1-hour
lifetime don't fail polling with a 401 Unauthorized.
"""

from __future__ import annotations

import argparse
import base64
import datetime
import json
import os
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

TOKEN_TTL_SECONDS = 2700  # Refresh token after 45 minutes (before 1 hour expiry)

def base64_url_encode(data: bytes) -> str:
    """Encode bytes using base64url encoding without padding."""
    return base64.urlsafe_b64encode(data).decode("ascii").rstrip("=")

def sign_app_jwt(client_id: str, private_key: str) -> str:
    """Create a 10-minute JWT signed with RS256 for GitHub App authentication."""
    now = int(time.time())
    iat = now - 60  # Tolerate clock skew with the GitHub API server
    exp = now + 540  # Max 10 minutes allowed by GitHub

    header = {"alg": "RS256", "typ": "JWT"}
    payload = {"iat": iat, "exp": exp, "iss": client_id}

    header_base64 = base64_url_encode(json.dumps(header, separators=(",", ":")).encode("utf-8"))
    payload_base64 = base64_url_encode(json.dumps(payload, separators=(",", ":")).encode("utf-8"))
    unsigned = f"{header_base64}.{payload_base64}"

    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8") as key_file:
        key_file.write(private_key)
        key_file.flush()
        process = subprocess.run(
            ["openssl", "dgst", "-sha256", "-sign", key_file.name],
            input=unsigned.encode("ascii"),
            capture_output=True,
            check=True,
        )
    signature_b64 = base64_url_encode(process.stdout)
    return f"{unsigned}.{signature_b64}"

def api_request(
    method: str,
    url: str,
    token: str,
    data: dict[str, Any] | None = None,
) -> Any:
    """Perform an authenticated HTTP JSON request to the GitHub API."""
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "User-Agent": "dispatch-and-poll-action",
    }
    encoded_data = None

    if data is not None:
        headers["Content-Type"] = "application/json"
        encoded_data = json.dumps(data).encode("utf-8")

    request = urllib.request.Request(url, data=encoded_data, headers=headers, method=method)

    try:
        with urllib.request.urlopen(request) as response:
            content = response.read()
            if content:
                return json.loads(content.decode("utf-8"))
            return None
    except urllib.error.HTTPError as err:
        body = err.read().decode("utf-8", errors="replace")
        print(f"::error::GitHub API request failed ({method} {url}) with HTTP {err.code}", file=sys.stderr, flush=True)
        if body:
            print(body, file=sys.stderr, flush=True)
        raise
    except urllib.error.URLError as err:
        print(f"::error::GitHub API request failed ({method} {url}): {err.reason}", file=sys.stderr, flush=True)
        raise

def mint_app_token(client_id: str, private_key: str, api_url: str, owner_repo: str) -> str:
    """Obtain an installation access token for the specified repository."""
    jwt = sign_app_jwt(client_id, private_key)
    installation_response = api_request("GET", f"{api_url}/repos/{owner_repo}/installation", jwt)
    installation_id = installation_response["id"]

    token_response = api_request(
        "POST",
        f"{api_url}/app/installations/{installation_id}/access_tokens",
        jwt,
        {
            "repositories": [owner_repo.rsplit("/", maxsplit=1)[-1]],
            "permissions": {"actions": "write"},
        },
    )
    return str(token_response["token"])

class TokenManager:
    """Manages creation and automatic refresh of GitHub App installation tokens."""
    def __init__(self, client_id: str, private_key: str, api_url: str, owner_repo: str) -> None:
        self.client_id = client_id
        self.private_key = private_key
        self.api_url = api_url
        self.owner_repo = owner_repo
        self.token: str = ""
        self.token_issued_at: float = 0.0
        self.refresh()

    def refresh(self) -> None:
        self.token = mint_app_token(self.client_id, self.private_key, self.api_url, self.owner_repo)
        self.token_issued_at = time.time()

    def get_token(self) -> str:
        if time.time() - self.token_issued_at > TOKEN_TTL_SECONDS:
            print("Refreshing GitHub App installation token before it expires...", flush=True)
            self.refresh()
        return self.token

def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse and validate command line arguments."""
    parser = argparse.ArgumentParser(description="Dispatches a workflow_dispatch run in a repository and poll it until completion.")
    parser.add_argument("--app-client-id", required=True, help="GitHub App client ID")
    parser.add_argument("--api-url", required=True, help="GitHub API URL")
    parser.add_argument("--owner-repo", required=True, help="Repository name with owner")
    parser.add_argument("--ref", required=True, help="The branch, tag or SHA")
    parser.add_argument("--workflow-file", required=True, help="Workflow file name")
    parser.add_argument("--payload-inputs-json", default="{}", help="JSON object string of inputs for the workflow_dispatch")
    parser.add_argument("--poll-interval-seconds", type=int, default=15, help="Poll interval seconds")
    return parser.parse_args(argv)

def poll_workflow_run(
    api_url: str,
    owner_repo: str,
    run_id: int | str,
    run_url: str,
    poll_interval_seconds: int,
    token_manager: TokenManager
) -> bool:
    """Poll a workflow run until completion, returning True on success or False on failure."""
    print(f"Polling run {run_id} until completion...", flush=True)

    while True:
        time.sleep(poll_interval_seconds)
        run_info = api_request("GET", f"{api_url}/repos/{owner_repo}/actions/runs/{run_id}", token_manager.get_token())
        status = run_info.get("status", "")
        conclusion = run_info.get("conclusion", "") # or ""

        print(f"status: {status}", flush=True)

        if status == "completed":
            print(f"conclusion: {conclusion}", flush=True)

            outputs = {
                "run_id": run_id,
                "run_number": run_info.get("run_number"),
                "run_name": run_info.get("name"),
                "status": status,
                "conclusion": conclusion,
                "workflow_id": run_info.get("workflow_id")
            }
            output_path = os.environ.get("GITHUB_OUTPUT")
            
            if output_path:
                with open(output_path, "a", encoding="utf-8") as output_file:
                    for output_name, output_value in outputs.items():
                        value = "" if output_value is None else str(output_value)
                        delimiter = os.urandom(16).hex()
                        output_file.write(f"{output_name}<<{delimiter}\n{value}\n{delimiter}\n")

            if conclusion == "success":
                print("Workflow run succeeded", flush=True)
                return True
            print(f"::error::Workflow run concluded with: {conclusion}", file=sys.stderr, flush=True)
            return False

def dispatch_workflow_request(
    api_url: str,
    owner_repo: str,
    workflow_file: str,
    trigger_ref: str,
    payload_inputs: dict[str, Any],
    token_manager: TokenManager,
) -> int | str | None:
    """Dispatch a workflow and return its run ID when the API provides one."""
    url = f"{api_url}/repos/{owner_repo}/actions/workflows/{workflow_file}/dispatches"
    body = {
        "ref": trigger_ref,
        "inputs": payload_inputs,
        "return_run_details": True,
    }

    print(f"Dispatch workflow '{workflow_file}' on the repo '{owner_repo}'", flush=True)
    print(f"POST: {url}", flush=True)

    response = api_request("POST", url, token_manager.get_token(), body)

    if isinstance(response, dict) and response.get("workflow_run_id"):
        return response["workflow_run_id"]
    return None

def dispatch_and_wait_for_workflow(
    api_url: str,
    owner_repo: str,
    workflow_file: str,
    trigger_ref: str,
    payload_inputs: dict[str, Any],
    token_manager: TokenManager,
    max_attempts: int = 30,
    poll_interval_seconds: int = 10,
) -> int | str | None:
    """Dispatch a workflow and find the resulting run ID."""
    dispatch_time = (datetime.datetime.now(datetime.UTC) - datetime.timedelta(minutes=2)).strftime("%Y-%m-%dT%H:%M:%SZ")

    run_id = dispatch_workflow_request(
        api_url,
        owner_repo,
        workflow_file,
        trigger_ref,
        payload_inputs,
        token_manager)

    if run_id:
        return run_id

    print("Waiting for the dispatched run to appear...", flush=True)

    runs_query_url = (
        f"{api_url}/repos/{owner_repo}/actions/workflows/{workflow_file}/runs"
        f"?event=workflow_dispatch&branch={urllib.parse.quote(trigger_ref)}&created=%3E{dispatch_time}&per_page=10")

    for attempt in range(1, max_attempts + 1):
        time.sleep(poll_interval_seconds)
        runs_resp = api_request("GET", runs_query_url, token_manager.get_token())
        workflow_runs = runs_resp.get("workflow_runs", []) if isinstance(runs_resp, dict) else []
        matching = [r for r in workflow_runs if r.get("head_branch") == trigger_ref]
        if matching:
            found_id = matching[0].get("id")
            print(f"Found dispatched run: {found_id}", flush=True)
            return found_id
        print(f"Run not found yet (attempt {attempt})...", flush=True)

    return None

def main(argv: list[str] | None = None) -> int:
    """Dispatches a workflow run and wait for it to finish.

    Authenticates via a GitHub App, dispatches the workflow with the provided inputs,
    locates the resulting run ID, and polls until completion. Returns 0 on success
    or 1 on error/failure.
    """

    args = parse_args(argv)
    api_url = args.api_url.rstrip("/")
    app_private_key = os.environ.get("APP_PRIVATE_KEY", "")

    if not app_private_key:
        print("::error::APP_PRIVATE_KEY environment variable is required", file=sys.stderr, flush=True)
        return 1

    try:
        payload_inputs = json.loads(args.payload_inputs_json)
        if not isinstance(payload_inputs, dict):
            msg = "payload_inputs_json must be a JSON object"
            raise TypeError(msg)
    except (json.JSONDecodeError, TypeError) as err:
        print(f"::error::payload_inputs_json must be a valid JSON object string: {err}", file=sys.stderr, flush=True)
        return 1

    token_manager = TokenManager(args.app_client_id, app_private_key, api_url, args.owner_repo)

    run_id = dispatch_and_wait_for_workflow(
        api_url=api_url,
        owner_repo=args.owner_repo,
        workflow_file=args.workflow_file,
        trigger_ref=args.ref,
        payload_inputs=payload_inputs,
        token_manager=token_manager
    )

    if not run_id:
        print("::error::Could not locate the triggered downstream workflow run", file=sys.stderr, flush=True)
        return 1

    run_detail = api_request("GET", f"{api_url}/repos/{args.owner_repo}/actions/runs/{run_id}", token_manager.get_token())
    run_url = run_detail.get("html_url", "")

    print(f"Workflow run: {run_url}", flush=True)

    if not poll_workflow_run(
        api_url=api_url,
        owner_repo=args.owner_repo,
        run_id=run_id,
        run_url=run_url,
        poll_interval_seconds=args.poll_interval_seconds,
        token_manager=token_manager
    ):
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
