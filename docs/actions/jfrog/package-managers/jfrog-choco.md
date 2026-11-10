# Action `jfrog-choco`

The [`jfrog-choco`](../../../../.github/actions/jfrog/package-managers/jfrog-choco/action.yml) action runs Chocolatey with optional JFrog build info collection.

## Inputs

| Name           | Required | Default | Description                                                                                                                                                                                                                                                                                                                                                                                               |
| -------------- | -------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `args`         | yes      |         | The `choco` arguments.                                                                                                                                                                                                                                                                                                                                                                                    |
| `build-name`   | no       |         | Providing this option will collect and record build info for this build name. Build number option is mandatory when this option is provided.                                                                                                                                                                                                                                                              |
| `build-number` | no       |         | Providing this option will collect and record build info for this build number. Build name option is mandatory when this option is provided.                                                                                                                                                                                                                                                              |
| `module`       | no       |         | Optional module name for the build info. Build name and number options are mandatory when this option is provided.                                                                                                                                                                                                                                                                                        |
| `project`      | no       |         | JFrog Artifactory project key.                                                                                                                                                                                                                                                                                                                                                                            |
| `repo`         | no       |         | Specifies the Artifactory repository name for the selected package manager, replacing the interactive repository selection. The interactive selection offers virtual repositories of the matching package type, which is normally what this should be set to. Note that `gradle` matches the `gradle` package type rather than `maven`, and `pip`, `pipenv`, `poetry`, `twine` and `uv` all match `pypi`. |
| `repo-resolve` | no       |         | Repository for dependencies resolution.                                                                                                                                                                                                                                                                                                                                                                   |
| `server-id`    | no       |         | Server ID configured using the `jf config` command.                                                                                                                                                                                                                                                                                                                                                       |
| `shell`        | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`.                                                                                                                                                                                                                                                                                                                          |

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

  - uses: $/.github/actions/jfrog/package-managers/jfrog-choco
    with:
      args: ...
```
