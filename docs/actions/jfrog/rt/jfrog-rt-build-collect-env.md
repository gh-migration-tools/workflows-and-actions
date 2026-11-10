# Action `jfrog-rt-build-collect-env`

The [`jfrog-rt-build-collect-env`](../../../../.github/actions/jfrog/rt/jfrog-rt-build-collect-env/action.yml) action collects environment variables. Environment variables can be excluded using the `build-publish` command.

## Inputs

| Name           | Required | Default | Description                                                                      |
| -------------- | -------- | ------- | -------------------------------------------------------------------------------- |
| `build-name`   | yes      |         | Build name.                                                                      |
| `build-number` | yes      |         | Build number.                                                                    |
| `project`      | no       |         | JFrog Artifactory project key.                                                   |
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

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-build-collect-env
    with:
      build-name: ...
      build-number: ...
```
