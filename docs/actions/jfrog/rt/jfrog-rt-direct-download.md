# Action `jfrog-rt-direct-download`

The [`jfrog-rt-direct-download`](../../../../.github/actions/jfrog/rt/jfrog-rt-direct-download/action.yml) action download files using direct API respecting Artifactory's native resolution order and bypassing AQL.

## Inputs

| Name                        | Required | Default | Description                                                                                                                                                                                                                                                                                                                 |
| --------------------------- | -------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `source-pattern`            | yes      |         | The source pattern in Artifactory that describes the artifacts to be downloaded.                                                                                                                                                                                                                                            |
| `target-pattern`            | yes      |         | The local file system path to which the artifacts should be downloaded. Default: `.`.                                                                                                                                                                                                                                       |
| `format`                    | no       |         | Defines the output format of the command. Acceptable values are: `json`, `table`.                                                                                                                                                                                                                                           |
| `access-token`              | no       |         | JFrog access token.                                                                                                                                                                                                                                                                                                         |
| `build`                     | no       |         | If specified, only artifacts of the specified build are matched. The property format is `build-name/build-number`. If you do not specify the build number, the artifacts are filtered by the latest build number. If the build is assigned to a specific project please provide the project key using the `--project` flag. |
| `build-name`                | no       |         | Providing this option will collect and record build info for this build name. Build number option is mandatory when this option is provided.                                                                                                                                                                                |
| `build-number`              | no       |         | Providing this option will collect and record build info for this build number. Build name option is mandatory when this option is provided.                                                                                                                                                                                |
| `bundle`                    | no       |         | If specified, only artifacts of the specified bundle are matched. The value format is `bundle-name/bundle-version`.                                                                                                                                                                                                         |
| `bypass-archive-inspection` | no       | `false` | Set to `true` to bypass the archive security inspection before it is unarchived. Used with the `explode` option.                                                                                                                                                                                                            |
| `client-cert-key-path`      | no       |         | Private key file for the client certificate in PEM format.                                                                                                                                                                                                                                                                  |
| `client-cert-path`          | no       |         | Client certificate file in PEM format.                                                                                                                                                                                                                                                                                      |
| `detailed-summary`          | no       | `false` | Set to `true` to include a list of the affected files in the command summary.                                                                                                                                                                                                                                               |
| `dry-run`                   | no       | `false` | Set to `true` to disable communication with Artifactory.                                                                                                                                                                                                                                                                    |
| `exclude-artifacts`         | no       |         | If specified, build artifacts are not matched. Used together with the `--build` flag.                                                                                                                                                                                                                                       |
| `exclusions`                | no       |         | List of semicolon-separated (`;`) exclusions. Exclusions can include the `*` and the `?` wildcards.                                                                                                                                                                                                                         |
| `explode`                   | no       | `false` | Set to `true` to extract an archive after it is downloaded from Artifactory.                                                                                                                                                                                                                                                |
| `fail-no-op`                | no       | `false` | Set to `true` if you'd like the command to return exit code 2 in case of no files are affected.                                                                                                                                                                                                                             |
| `flat`                      | no       | `false` | Set to `true` if you do not wish to have the Artifactory repository path structure created locally for your downloaded files.                                                                                                                                                                                               |
| `include-deps`              | no       |         | If specified, also dependencies of the specified build are matched. Used together with the `--build` flag.                                                                                                                                                                                                                  |
| `insecure-tls`              | no       | `false` | Set to `true` to skip TLS certificates verification.                                                                                                                                                                                                                                                                        |
| `min-split`                 | no       |         | Minimum file size in KB to split into ranges when downloading. Set to `-1` for no splits.                                                                                                                                                                                                                                   |
| `module`                    | no       |         | Optional module name for the build info. Build name and number options are mandatory when this option is provided.                                                                                                                                                                                                          |
| `password`                  | no       |         | JFrog password.                                                                                                                                                                                                                                                                                                             |
| `project`                   | no       |         | JFrog Artifactory project key.                                                                                                                                                                                                                                                                                              |
| `quiet`                     | no       | `false` | Set to `true` to skip the sync-deletes confirmation message.                                                                                                                                                                                                                                                                |
| `recursive`                 | no       |         | Set to `false` if you do not wish to include the download of artifacts inside sub-folders in Artifactory.                                                                                                                                                                                                                   |
| `retries`                   | no       |         | Number of HTTP retries.                                                                                                                                                                                                                                                                                                     |
| `retry-wait-time`           | no       |         | Number of seconds or milliseconds to wait between retries. The numeric value should either end with s for seconds or ms for milliseconds (for example: `10s` or `100ms`).                                                                                                                                                   |
| `server-id`                 | no       |         | Server ID configured using the `jf config` command.                                                                                                                                                                                                                                                                         |
| `skip-checksum`             | no       | `false` | Set to `true` to skip checksum verification when downloading.                                                                                                                                                                                                                                                               |
| `spec`                      | no       |         | Path to a File Spec.                                                                                                                                                                                                                                                                                                        |
| `spec-json`                 | no       |         | Spec as JSON.                                                                                                                                                                                                                                                                                                               |
| `spec-vars`                 | no       |         | List of semicolon-separated (`;`) variables in the form of `key1=value1;key2=value2;...` (wrapped by quotes) to be replaced in the File Spec. In the File Spec, the variables should be used as follows: `${key1}`.                                                                                                         |
| `split-count`               | no       |         | Number of parts to split a file when downloading. Set to `0` for no splits.                                                                                                                                                                                                                                                 |
| `ssh-key-path`              | no       |         | SSH key file path.                                                                                                                                                                                                                                                                                                          |
| `ssh-passphrase`            | no       |         | SSH key passphrase.                                                                                                                                                                                                                                                                                                         |
| `sync-deletes`              | no       |         | Specific path in the local file system, under which to sync dependencies after the download. After the download, this path will include only the dependencies downloaded during this download operation. The other files under this path will be deleted.                                                                   |
| `threads`                   | no       |         | Number of working threads.                                                                                                                                                                                                                                                                                                  |
| `url`                       | no       |         | JFrog Platform URL. (example: `https://acme.jfrog.io`)                                                                                                                                                                                                                                                                      |
| `user`                      | no       |         | JFrog username.                                                                                                                                                                                                                                                                                                             |
| `validate-symlinks`         | no       | `false` | Set to `true` to perform a checksum validation when downloading symbolic links.                                                                                                                                                                                                                                             |
| `shell`                     | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`.                                                                                                                                                                                                                                            |

## Outputs

| Name      | Description        |
| --------- | ------------------ |
| `command` | The JFrog command. |

## Examples

### Basic

```yaml
steps:
  - name: Setup JFrog CLI
    uses: jfrog/setup-jfrog-cli@v5.3.4
    env:
      JF_URL: ${{ vars.JF_URL }}
      JF_ACCESS_TOKEN: ${{ secrets.JF_ACCESS_TOKEN }}

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-direct-download
    with:
      source-pattern: ...
      target-pattern: ...
```

### With spec JSON

```yaml
steps:
  - name: Setup JFrog CLI
    uses: jfrog/setup-jfrog-cli@v5.3.4
    env:
      JF_URL: ${{ vars.JF_URL }}
      JF_ACCESS_TOKEN: ${{ secrets.JF_ACCESS_TOKEN }}

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-direct-download
    with:
      source-pattern: ...
      target-pattern: ...
      spec-json: |
        {
          "files": []
        }
```
