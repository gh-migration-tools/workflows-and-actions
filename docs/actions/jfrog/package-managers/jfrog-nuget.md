# Action `jfrog-nuget`

The [`jfrog-nuget`](../../../../.github/actions/jfrog/package-managers/jfrog-nuget/action.yml) action runs NuGet.

## Inputs

| Name                         | Required | Default | Description                                                                                                                                                                                                                                                                                                                                                                                               |
| ---------------------------- | -------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `args`                       | yes      |         | The `nuget` arguments.                                                                                                                                                                                                                                                                                                                                                                                    |
| `allow-insecure-connections` | no       | `false` | Set to `true` if you wish to configure NuGet sources with unsecured connections. This is recommended for testing purposes only.                                                                                                                                                                                                                                                                           |
| `build-name`                 | no       |         | Providing this option will collect and record build info for this build name. Build number option is mandatory when this option is provided.                                                                                                                                                                                                                                                              |
| `build-number`               | no       |         | Providing this option will collect and record build info for this build number. Build name option is mandatory when this option is provided.                                                                                                                                                                                                                                                              |
| `module`                     | no       |         | Optional module name for the build info. Build name and number options are mandatory when this option is provided.                                                                                                                                                                                                                                                                                        |
| `nuget-v2`                   | no       | `false` | Set to `true` if you'd like to use the NuGet V2 protocol when restoring packages from Artifactory.                                                                                                                                                                                                                                                                                                        |
| `project`                    | no       |         | JFrog Artifactory project key.                                                                                                                                                                                                                                                                                                                                                                            |
| `repo`                       | no       |         | Specifies the Artifactory repository name for the selected package manager, replacing the interactive repository selection. The interactive selection offers virtual repositories of the matching package type, which is normally what this should be set to. Note that `gradle` matches the `gradle` package type rather than `maven`, and `pip`, `pipenv`, `poetry`, `twine` and `uv` all match `pypi`. |
| `repo-resolve`               | no       |         | Repository for dependencies resolution.                                                                                                                                                                                                                                                                                                                                                                   |
| `server-id`                  | no       |         | Server ID configured using the `jf config` command.                                                                                                                                                                                                                                                                                                                                                       |
| `shell`                      | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`.                                                                                                                                                                                                                                                                                                                          |

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

  - uses: $/.github/actions/jfrog/package-managers/jfrog-nuget
    with:
      args: ...
```
