# Action `jfrog-nuget-config`

The [`jfrog-nuget-config`](../../../../.github/actions/jfrog/package-managers/jfrog-nuget-config/action.yml) action generates `nuget` configuration.

## Inputs

| Name                | Required | Default | Description                                                                                                                 |
| ------------------- | -------- | ------- | --------------------------------------------------------------------------------------------------------------------------- |
| `global`            | no       | `false` | Set to `true` to make the configuration global (for all projects). Specific projects can override the global configuration. |
| `nuget-v2`          | no       | `false` | Set to `true` if you'd like to use the NuGet V2 protocol when restoring packages from Artifactory.                          |
| `repo-resolve`      | no       |         | Repository for dependencies resolution.                                                                                     |
| `server-id-resolve` | no       |         | Artifactory server ID for resolution. The server should be configured using the `jfrog c add` command.                      |
| `shell`             | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`.                                            |

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

  - uses: $/.github/actions/jfrog/package-managers/jfrog-nuget-config
```
