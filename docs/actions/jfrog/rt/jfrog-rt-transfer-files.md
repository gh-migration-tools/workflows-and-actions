# Action `jfrog-rt-transfer-files`

The [`jfrog-rt-transfer-files`](../../../../.github/actions/jfrog/rt/jfrog-rt-transfer-files/action.yml) action transfer files from one Artifactory to another.

## Inputs

| Name               | Required | Default | Description                                                                                                                                                                                                                                                          |
| ------------------ | -------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `source-server-id` | yes      |         | Server ID of the Artifactory instance to transfer from.                                                                                                                                                                                                              |
| `target-server-id` | yes      |         | Server ID of the Artifactory instance to transfer to.                                                                                                                                                                                                                |
| `created-after`    | no       |         | Transfer only files created at or after this exact UTC timestamp. Format: `YYYY-MM-DDTHH:mm:ss.sssZ`. When both `--created-after` and `--downloaded-after` are set, `--created-after` takes precedence.                                                              |
| `downloaded-after` | no       |         | Transfer only files last downloaded at or after this exact UTC timestamp. Format: `YYYY-MM-DDTHH:mm:ss.sssZ`. Files that were never downloaded are excluded. Ignored when `--created-after` is also set.                                                             |
| `exclude-repos`    | no       |         | List of semicolon-separated (`;`) repositories to exclude from the transfer. You can use wildcards to specify patterns for the repositories' names.                                                                                                                  |
| `filestore`        | no       | `false` | Set to `true` to make the transfer mechanism check for the existence of artifacts on the target filestore. Used when the files are already expected to be located on the filestore.                                                                                  |
| `format`           | no       |         | Defines the output format of the command. Acceptable values are: `json`, `table`.                                                                                                                                                                                    |
| `ignore-state`     | no       | `false` | Set to `true` to ignore the saved state from previous `transfer-files` operations.                                                                                                                                                                                   |
| `include-files`    | no       |         | List of semicolon-separated (`;`) path patterns to include in the transfer. Files will be filtered based on their directory path. Pattern examples: `folder/subfolder/*`, `org/company/*`.                                                                           |
| `include-repos`    | no       |         | List of semicolon-separated (`;`) repositories to include in the transfer. You can use wildcards to specify patterns for the repositories' names.                                                                                                                    |
| `prechecks`        | no       | `false` | Set to `true` to run pre-transfer checks.                                                                                                                                                                                                                            |
| `proxy-key`        | no       |         | The key of an HTTP proxy configuration in Artifactory. This proxy will be used for the transfer traffic between the source and target instances. To configure this proxy, go to _"Proxies \| Configuration \| Proxy Configuration"_  in the JFrog Administration UI. |
| `status`           | no       | `false` | Set to `true` to show the status of the `transfer-files` command currently in progress.                                                                                                                                                                              |
| `stop`             | no       | `false` | Set to `true` to stop the `transfer-files` command currently in progress. Useful when running the `transfer-files` command in the background.                                                                                                                        |
| `shell`            | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`.                                                                                                                                                                                     |

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

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-transfer-files
    with:
      source-server-id: ...
      target-server-id: ...
```
