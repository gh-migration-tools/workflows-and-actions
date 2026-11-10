# Action `jfrog-npm`

The [`jfrog-npm`](../../../../.github/actions/jfrog/package-managers/jfrog-npm/action.yml) action runs `npm` command.

## Inputs

| Name    | Required | Default | Description                                                                      |
| ------- | -------- | ------- | -------------------------------------------------------------------------------- |
| `args`  | yes      |         | The `npm` arguments.                                                             |
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

  - uses: $/.github/actions/jfrog/package-managers/jfrog-npm
    with:
      args: ...
```
