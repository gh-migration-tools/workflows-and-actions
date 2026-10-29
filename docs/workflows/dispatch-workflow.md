# Workflow `dispatch_workflow`

The [`dispatch-workflow`](../../.github/workflows/dispatch-workflow.yml) workflow dispatches a `workflow_dispatch` workflow run in a repository and polls it until completion, refreshing its GitHub App token as needed for long-running downstream runs.

> [!IMPORTANT]
> This action requires an GitHub App with the following permissions:
>
> - Actions: `Read and write`
> - Contents: `Read and write`
> - Deployments: `Read-only`
> - Pull requests: `Read and write`

## Events

This reusable workflow is invoked by another workflow using `workflow_call`.

## Inputs

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `client-id` | string | yes |  | GitHub App client ID |
| `api-url` | string | no | `https://api.github.com` | GitHub API URL |
| `owner-repo` | string | yes |  | Repository name with owner |
| `ref` | string | yes |  | The branch, tag or SHA |
| `workflow-file` | string | yes |  | Workflow file name |
| `payload-inputs-json` | string | no | `{}` | JSON object string passed as workflow_dispatch inputs |
| `poll-interval-seconds` | string | no | `15` | Poll interval seconds |
| `runner` | string | no | `ubuntu-latest` | The runner label |
| `timeout-minutes` | number | no | `360` | The runner timeout |

## Secrets

| Name | Required | Description |
| --- | --- | --- |
| `private-key` | yes | GitHub App private key |

## Outputs

| Name | Description |
| --- | --- |
| `run-id` | The run ID |
| `run-number` | The run number |
| `run-name` | The run name |
| `status` | The run status |
| `conclusion` | The run conclusion |
| `workflow-id` | The workflow ID |

## Example

```yaml
jobs:
  dispatch_workflow:
    uses: $/.github/workflows/dispatch-workflow.yml
    with:
      client-id: ${{ vars.GITHUB_APP_CLIENT_ID }}
      owner-repo: owner/repo
      ref: main
      workflow-file: workflow.yml
      payload-inputs-json: |
        {
          "firstname": "John",
          "lastname": "Doe"
        }
    secrets:
      private-key: ${{ secrets.GITHUB_APP_PRIVATE_KEY }}

  show_outputs:
    needs: dispatch_workflow
    runs-on: ubuntu-latest
    steps:
      - name: Show outputs
        env:
          RUN_ID: ${{ needs.dispatch_workflow.outputs.run-id }}
          RUN_NUMBER: ${{ needs.dispatch_workflow.outputs.run-number }}
          RUN_NAME: ${{ needs.dispatch_workflow.outputs.run-name }}
          STATUS: ${{ needs.dispatch_workflow.outputs.status }}
          CONCLUSION: ${{ needs.dispatch_workflow.outputs.conclusion }}
          WORKFLOW_ID: ${{ needs.dispatch_workflow.outputs.workflow-id }}
        run: |
          echo "${RUN_ID} / ${RUN_NUMBER}"
```