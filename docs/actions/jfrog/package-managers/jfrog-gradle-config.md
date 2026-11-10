# Action `jfrog-gradle-config`

The [`jfrog-gradle-config`](../../../../.github/actions/jfrog/package-managers/jfrog-gradle-config/action.yml) action generates `gradle` build configuration.

## Inputs

| Name                    | Required | Default | Description                                                                                                                 |
| ----------------------- | -------- | ------- | --------------------------------------------------------------------------------------------------------------------------- |
| `deploy-ivy-desc`       | no       |         | Set to `false` if you don't wish to deploy Ivy descriptors.                                                                 |
| `deploy-maven-desc`     | no       |         | Set to `false` if you don't wish to deploy Maven descriptors.                                                               |
| `global`                | no       | `false` | Set to `true` to make the configuration global (for all projects). Specific projects can override the global configuration. |
| `ivy-artifacts-pattern` | no       |         | `/[module]/[revision]/[artifact]-[revision](-[classifier]).[ext]` Set the deployed Ivy artifacts pattern.                   |
| `ivy-desc-pattern`      | no       |         | `/[module]/ivy-[revision].xml` Set the deployed Ivy descriptor pattern.                                                     |
| `repo-deploy`           | no       |         | Repository for artifacts deployment.                                                                                        |
| `repo-resolve`          | no       |         | Repository for dependencies resolution.                                                                                     |
| `server-id-deploy`      | no       |         | Artifactory server ID for deployment. The server should be configured using the `jfrog c add` command.                      |
| `server-id-resolve`     | no       |         | Artifactory server ID for resolution. The server should be configured using the `jfrog c add` command.                      |
| `use-wrapper`           | no       | `false` | Set to `true` to use the wrapper.                                                                                           |
| `uses-plugin`           | no       | `false` | Set to `true` if the Gradle Artifactory Plugin is already applied in the build script.                                      |
| `shell`                 | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`.                                            |

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

  - uses: $/.github/actions/jfrog/package-managers/jfrog-gradle-config
```
