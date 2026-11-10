# Action `jfrog-terraform-config`

The [`jfrog-terraform-config`](../../../../.github/actions/jfrog/package-managers/jfrog-terraform-config/action.yml) action generates Terraform configuration.

## Inputs

| Name               | Required | Default | Description                                                                                                                 |
| ------------------ | -------- | ------- | --------------------------------------------------------------------------------------------------------------------------- |
| `global`           | no       | `false` | Set to `true` to make the configuration global (for all projects). Specific projects can override the global configuration. |
| `repo-deploy`      | no       |         | Repository for artifacts deployment.                                                                                        |
| `server-id-deploy` | no       |         | Artifactory server ID for deployment. The server should be configured using the `jfrog c add` command.                      |
| `shell`            | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`.                                            |

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

  - uses: $/.github/actions/jfrog/package-managers/jfrog-terraform-config
```
