# Action `jfrog-mvn-config`

The [`jfrog-mvn-config`](../../../../.github/actions/jfrog/package-managers/jfrog-mvn-config/action.yml) action generates `maven` build configuration.

## Inputs

| Name                      | Required | Default | Description                                                                                                                                               |
| ------------------------- | -------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `disable-snapshots`       | no       | `false` | Set to `true` to disable snapshot resolution.                                                                                                             |
| `exclude-patterns`        | no       |         | Filter deployed artifacts by setting a wildcard pattern that specifies which artifacts to exclude. You may provide multiple patterns separated by `', '`. |
| `global`                  | no       | `false` | Set to `true` to make the configuration global (for all projects). Specific projects can override the global configuration.                               |
| `include-patterns`        | no       |         | Filter deployed artifacts by setting a wildcard pattern that specifies which artifacts to include. You may provide multiple patterns separated by `', '`. |
| `repo-deploy-releases`    | no       |         | Deployment repository for release artifacts.                                                                                                              |
| `repo-deploy-snapshots`   | no       |         | Deployment repository for snapshot artifacts.                                                                                                             |
| `repo-resolve-releases`   | no       |         | Resolution repository for release dependencies.                                                                                                           |
| `repo-resolve-snapshots`  | no       |         | Resolution repository for snapshot dependencies.                                                                                                          |
| `server-id-deploy`        | no       |         | Artifactory server ID for deployment. The server should be configured using the `jfrog c add` command.                                                    |
| `server-id-resolve`       | no       |         | Artifactory server ID for resolution. The server should be configured using the `jfrog c add` command.                                                    |
| `snapshots-update-policy` | no       |         | Set snapshot update policy. Defaults to daily.                                                                                                            |
| `use-wrapper`             | no       | `false` | Set to `true` to use the wrapper.                                                                                                                         |
| `shell`                   | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`.                                                                          |

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

  - uses: $/.github/actions/jfrog/package-managers/jfrog-mvn-config
```
