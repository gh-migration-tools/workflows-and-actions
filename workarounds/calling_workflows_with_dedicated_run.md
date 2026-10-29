# Calling workflows with dedicated run

GitHub Actions **do not** support calling a workflow and running it in a dedicated run. Called workflows with the `workflow_call` event are executed in the context of the calling workflow and **do not** create a dedicated run. And workflows with the `workflow_dispatch` event can only be dispatched using the GitHub API (_fire-and-forget_) and **do not** provided any feedback for the dispatched workflow in the calling workflow.

To get around this limitation use the `dispatch-workflow` action or workflow.

The `dispatch-workflow` action or workflow dispatches a `workflow_dispatch` workflow run in a repository and polls it until completion, refreshing its GitHub App token as needed for long-running downstream runs.

- Documentation [action](../docs/actions/dispatch-workflow.md) / [workflow](../docs/workflows/dispatch-workflow.md)
- Source [action](../.github/actions/dispatch-workflow/action.yml) / [workflow](../.github/workflows/dispatch-workflow.yml)

## Examples

### With action

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

### With workflow

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