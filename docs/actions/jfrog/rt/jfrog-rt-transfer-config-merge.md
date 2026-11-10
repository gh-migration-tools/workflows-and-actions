# Action `jfrog-rt-transfer-config-merge`

The [`jfrog-rt-transfer-config-merge`](../../../../.github/actions/jfrog/rt/jfrog-rt-transfer-config-merge/action.yml) action merges projects and repositories from a source Artifactory instance to a target Artifactory instance, if no conflicts are found.

## Inputs

| Name               | Required | Default | Description                                                                                                                                            |
| ------------------ | -------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `source-server-id` | yes      |         | The source server ID. The configuration will be exported from this server.                                                                             |
| `target-server-id` | yes      |         | The target server ID. The configuration will be imported to this server.                                                                               |
| `exclude-projects` | no       |         | List of semicolon-separated (`;`) JFrog Projects to exclude from the transfer. You can use wildcards to specify patterns for the project keys.         |
| `exclude-repos`    | no       |         | List of semicolon-separated (`;`) repositories to exclude from the transfer. You can use wildcards to specify patterns for the repositories' names.    |
| `format`           | no       |         | Defines the output format of the command. Acceptable values are: `json`, `table`.                                                                      |
| `include-projects` | no       |         | List of semicolon-separated (`;`) JFrog Project keys to include in the transfer. You can use wildcards to specify patterns for the JFrog Project keys. |
| `include-repos`    | no       |         | List of semicolon-separated (`;`) repositories to include in the transfer. You can use wildcards to specify patterns for the repositories' names.      |
| `shell`            | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`.                                                                       |

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

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-transfer-config-merge
    with:
      source-server-id: ...
      target-server-id: ...
```
