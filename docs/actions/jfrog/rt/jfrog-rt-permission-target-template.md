# Action `jfrog-rt-permission-target-template`

The [`jfrog-rt-permission-target-template`](../../../../.github/actions/jfrog/rt/jfrog-rt-permission-target-template/action.yml) action creates a JSON template for a permission target creation or replacement.

## Inputs

| Name            | Required | Default | Description                                                                      |
| --------------- | -------- | ------- | -------------------------------------------------------------------------------- |
| `template-path` | yes      |         | Specifies the local file system path for the template file.                      |
| `shell`         | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`. |

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

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-permission-target-template
    with:
      template-path: ...
```
