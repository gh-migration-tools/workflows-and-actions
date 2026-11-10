# Action `jfrog-mvn`

The [`jfrog-mvn`](../../../../.github/actions/jfrog/package-managers/jfrog-mvn/action.yml) action runs Maven build.

## Inputs

| Name                | Required | Default | Description                                                                                                                                                                                                                              |
| ------------------- | -------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `goals-and-options` | yes      |         | Goals and options to run with `mvn` command. For example `-f path/to/pom.xml`.                                                                                                                                                           |
| `build-name`        | no       |         | Providing this option will collect and record build info for this build name. Build number option is mandatory when this option is provided.                                                                                             |
| `build-number`      | no       |         | Providing this option will collect and record build info for this build number. Build name option is mandatory when this option is provided.                                                                                             |
| `detailed-summary`  | no       | `false` | Set to `true` to include a list of the affected files in the command summary.                                                                                                                                                            |
| `format`            | no       |         | Defines the output format of the command. Acceptable values are: `table`, `json`, `simple-json` and `sarif`. Note: the `json` format doesn't include information about scans that are included as part of the Advanced Security package. |
| `insecure-tls`      | no       | `false` | Set to `true` to skip TLS certificates verification.                                                                                                                                                                                     |
| `project`           | no       |         | JFrog Artifactory project key.                                                                                                                                                                                                           |
| `scan`              | no       | `false` | Set if you'd like all files to be scanned by Xray on the local file system prior to the upload, and skip the upload if any of the files are found vulnerable.                                                                            |
| `server-id`         | no       |         | Server ID configured using the `jf config` command. Used in native mode (`JFROG_RUN_NATIVE=true`) for build info operations (artifact tagging, virtual-repo resolution). Has no effect in legacy (`config-file`) mode.                   |
| `threads`           | no       |         | Number of threads for uploading build artifacts.                                                                                                                                                                                         |
| `shell`             | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`.                                                                                                                                                         |

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

  - uses: $/.github/actions/jfrog/package-managers/jfrog-mvn
    with:
      goals-and-options: ...
```
