# Action `jfrog-rt-transfer-settings`

The [`jfrog-rt-transfer-settings`](../../../../.github/actions/jfrog/rt/jfrog-rt-transfer-settings/action.yml) action configures the settings for the `jf rt transfer-files` command.

## Inputs

| Name    | Required | Default | Description                                                                      |
| ------- | -------- | ------- | -------------------------------------------------------------------------------- |
| `shell` | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`. |

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

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-transfer-settings
```
