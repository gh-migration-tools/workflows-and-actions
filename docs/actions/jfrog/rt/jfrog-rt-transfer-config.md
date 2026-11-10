# Action `jfrog-rt-transfer-config`

The [`jfrog-rt-transfer-config`](../../../../.github/actions/jfrog/rt/jfrog-rt-transfer-config/action.yml) action copy the full configuration from a source Artifactory server to a target server

## Inputs

| Name                 | Required | Default | Description                                                                                                                                         |
| -------------------- | -------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `source-server-id`   | yes      |         | The source server ID. The configuration will be exported from this server.                                                                          |
| `target-server-id`   | yes      |         | The target server ID. The configuration will be imported to this server.                                                                            |
| `exclude-repos`      | no       |         | List of semicolon-separated (`;`) repositories to exclude from the transfer. You can use wildcards to specify patterns for the repositories' names. |
| `force`              | no       | `false` | Set to `true` to allow config transfer to a non-empty Artifactory server.                                                                           |
| `format`             | no       |         | Defines the output format of the command. Acceptable values are: `json`.                                                                            |
| `include-repos`      | no       |         | List of semicolon-separated (`;`) repositories to include in the transfer. You can use wildcards to specify patterns for the repositories' names.   |
| `prechecks`          | no       | `false` | Set to `true` to run pre-transfer checks.                                                                                                           |
| `source-working-dir` | no       |         | Local working directory on the source Artifactory server.                                                                                           |
| `target-working-dir` | no       |         | Local working directory on the target Artifactory server.                                                                                           |
| `verbose`            | no       | `false` | Set to `true` to increase verbosity during the export configuration from the source Artifactory phase.                                              |
| `shell`              | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`.                                                                    |
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

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-transfer-config
    with:
      source-server-id: ...
      target-server-id: ...
```
