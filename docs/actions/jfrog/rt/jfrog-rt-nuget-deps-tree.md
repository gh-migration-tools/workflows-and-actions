# Action `jfrog-rt-nuget-deps-tree`

The [`jfrog-rt-nuget-deps-tree`](../../../../.github/actions/jfrog/rt/jfrog-rt-nuget-deps-tree/action.yml) action shows solution dependency tree.

## Inputs

| Name     | Required | Default | Description                                                                       |
| -------- | -------- | ------- | --------------------------------------------------------------------------------- |
| `format` | no       |         | Defines the output format of the command. Acceptable values are: `json`, `table`. |
| `shell`  | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`.  |

## Outputs

| Name      | Description        |
| --------- | ------------------ |
| `command` | The JFrog command. |

## Example

```yaml
steps:
  - name: Setup JFrog CLI
    uses: jfrog/setup-jfrog-cli@v5.3.4
    env:
      JF_URL: ${{ vars.JF_URL }}
      JF_ACCESS_TOKEN: ${{ secrets.JF_ACCESS_TOKEN }}

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-nuget-deps-tree
    with:
      format: table
```
