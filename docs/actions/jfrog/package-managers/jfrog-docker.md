# Action `jfrog-docker`

The [`jfrog-docker`](../../../../.github/actions/jfrog/package-managers/jfrog-docker/action.yml) action runs any `docker` command, including `jf docker scan` for scanning a local image with JFrog Xray.

## Inputs

| Name                    | Required | Default | Description                                                                                                                                                                                                                              |
| ----------------------- | -------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `args`                  | yes      |         | The `docker` arguments. Acceptable values are: `login`, `build`, `push`, `pull`, `scan`.                                                                                                                                                 |
| `build-name`            | no       |         | Providing this option will collect and record build info for this build name. Build number option is mandatory when this option is provided.                                                                                             |
| `build-number`          | no       |         | Providing this option will collect and record build info for this build number. Build name option is mandatory when this option is provided.                                                                                             |
| `bypass-archive-limits` | no       | `false` | Set to `true` to bypass the indexer-app archive limits.                                                                                                                                                                                  |
| `detailed-summary`      | no       | `false` | Set to `true` to include a list of the affected files in the command summary.                                                                                                                                                            |
| `extended-table`        | no       | `false` | Set to `true` if you'd like the table to include extended fields such as _CVSS_ & _Xray Issue Id_. Ignored if provided `format` is not `table`.                                                                                          |
| `fail`                  | no       |         | Set to `false` if you don't wish the command to return exit code 3, even if the _Fail Build_ rule is matched by Xray.                                                                                                                    |
| `fixable-only`          | no       |         | Set to `true` if you wish to display issues that have a fixed version only.                                                                                                                                                              |
| `format`                | no       |         | Defines the output format of the command. Acceptable values are: `table`, `json`, `simple-json` and `sarif`. Note: the `json` format doesn't include information about scans that are included as part of the Advanced Security package. |
| `licenses`              | no       | `false` | Set to `true` if you'd like to receive licenses from Xray scanning.                                                                                                                                                                      |
| `min-severity`          | no       |         | Set the minimum severity of issues to display. The following values are accepted: `Low`, `Medium`, `High` or `Critical`.                                                                                                                 |
| `module`                | no       |         | Optional module name for the build info. Build name and number options are mandatory when this option is provided.                                                                                                                       |
| `project`               | no       |         | JFrog Artifactory project key.                                                                                                                                                                                                           |
| `repo-path`             | no       |         | Target repo path, to enable Xray to determine watches accordingly.                                                                                                                                                                       |
| `server-id`             | no       |         | Server ID configured using the `jf config` command.                                                                                                                                                                                      |
| `skip-login`            | no       | `false` | Set to `true` if you'd like the command to skip performing login.                                                                                                                                                                        |
| `threads`               | no       |         | Number of working threads.                                                                                                                                                                                                               |
| `validate-sha`          | no       | `false` | Set to `true` to enable SHA validation during Docker push.                                                                                                                                                                               |
| `vuln`                  | no       | `false` | Set to `true` if you'd like to receive an additional view of all vulnerabilities, regardless of the policy configured in Xray. Ignored if provided `format` is `sarif`.                                                                  |
| `watches`               | no       |         | A comma-separated (`,`) list of Xray watches, to determine Xray's violations creation.                                                                                                                                                   |
| `shell`                 | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`.                                                                                                                                                         |

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

  - uses: $/.github/actions/jfrog/package-managers/jfrog-docker
    with:
      args: ...
```
