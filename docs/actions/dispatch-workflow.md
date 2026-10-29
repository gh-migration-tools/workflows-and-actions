# Action `dispatch-workflow`

The [`dispatch-workflow`](../../.github/actions/dispatch-workflow/action.yml) action dispatches a `workflow_dispatch` workflow run in a repository and polls it until completion, refreshing its GitHub App token as needed for long-running downstream runs.

> [!IMPORTANT]
> This action requires an GitHub App with the following permissions:
>
> - Actions: `Read and write`
> - Contents: `Read and write`
> - Deployments: `Read-only`
> - Pull requests: `Read and write`

## Inputs

| Name | Required | Default | Description |
| --- | --- | --- | --- |
| `client-id` | yes |  | GitHub App client ID |
| `private-key` | yes |  | GitHub App private key |
| `api-url` | no | `https://api.github.com` | GitHub API URL |
| `owner-repo` | yes |  | Repository name with owner |
| `ref` | yes |  | The branch, tag or SHA |
| `workflow-file` | yes |  | Workflow file name |
| `payload-inputs-json` | no | `{}` | JSON object string passed as `workflow_dispatch` inputs |
| `poll-interval-seconds` | no | `15` | Poll interval seconds |

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
steps:
  - name: Dispatch workflow
    id: dispatch_workflow
    uses: $/.github/actions/dispatch-workflow
    with:
      client-id: ${{ vars.GITHUB_APP_CLIENT_ID }}
      private-key: ${{ secrets.GITHUB_APP_PRIVATE_KEY }}
      owner-repo: owner/repo
      ref: main
      workflow-file: workflow.yml
      payload-inputs-json: |
        {
          "firstname": "John",
          "lastname": "Doe"
        }

  - name: Show outputs
    env:
      RUN_ID: ${{ steps.dispatch_workflow.outputs.run-id }}
      RUN_NUMBER: ${{ steps.dispatch_workflow.outputs.run-number }}
      RUN_NAME: ${{ steps.dispatch_workflow.outputs.run-name }}
      STATUS: ${{ steps.dispatch_workflow.outputs.status }}
      CONCLUSION: ${{ steps.dispatch_workflow.outputs.conclusion }}
      WORKFLOW_ID: ${{ steps.dispatch_workflow.outputs.workflow-id }}
    run: |
      echo "${RUN_ID} / ${RUN_NUMBER}"
```