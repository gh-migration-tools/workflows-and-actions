# Action `jfrog-rt-build-clean`

The [`jfrog-rt-build-clean`](../../../../.github/actions/jfrog/rt/jfrog-rt-build-clean/action.yml) action cleans (removes) build info collected locally.

## Inputs

| Name           | Required | Default | Description                                                                      |
| -------------- | -------- | ------- | -------------------------------------------------------------------------------- |
| `build-name`   | yes      |         | Build name.                                                                      |
| `build-number` | yes      |         | Build number.                                                                    |
| `shell`        | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`. |

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

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-build-clean
    with:
      build-name: ...
      build-number: ...
```
