# Action `jfrog-rt-upload`

The [`jfrog-rt-upload`](../../../../.github/actions/jfrog/rt/jfrog-rt-upload/action.yml) action uploads files from local file system to Artifactory.

## Inputs

| Name                   | Required | Default | Description                                                                                                                                                                                                                                              |
| ---------------------- | -------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `source-pattern`       | yes      |         | Specifies the local file system path to artifacts which should be uploaded to Artifactory.                                                                                                                                                               |
| `target-pattern`       | yes      |         | Specifies the target path in Artifactory in the following format: `<repository name>/<repository path>`.                                                                                                                                                 |
| `format`               | no       |         | Defines the output format of the command. Acceptable values are: `json`, `table`.                                                                                                                                                                        |
| `access-token`         | no       |         | JFrog access token.                                                                                                                                                                                                                                      |
| `ant`                  | no       | `false` | Set to `true` to use an ant pattern instead of wildcards expression to collect files to upload.                                                                                                                                                          |
| `archive`              | no       |         | Set to `zip` to pack and deploy the files to Artifactory inside a ZIP archive. Currently, the only packaging format supported is `zip`.                                                                                                                  |
| `build-name`           | no       |         | Providing this option will collect and record build info for this build name. Build number option is mandatory when this option is provided.                                                                                                             |
| `build-number`         | no       |         | Providing this option will collect and record build info for this build number. Build name option is mandatory when this option is provided.                                                                                                             |
| `chunk-size`           | no       |         | The upload chunk size in MiB that can be concurrently uploaded during a multi-part upload. This option, as well as the functionality of multi-part upload, requires Artifactory with S3 or GCP storage.                                                  |
| `client-cert-key-path` | no       |         | Private key file for the client certificate in PEM format.                                                                                                                                                                                               |
| `client-cert-path`     | no       |         | Client certificate file in PEM format.                                                                                                                                                                                                                   |
| `deb`                  | no       |         | Used for Debian packages in the form of distribution/component/architecture. If the value for distribution, component or architecture includes a slash, the slash should be escaped with a back-slash.                                                   |
| `detailed-summary`     | no       | `false` | Set to `true` to include a list of the affected files in the command summary.                                                                                                                                                                            |
| `dry-run`              | no       | `false` | Set to `true` to disable communication with Artifactory.                                                                                                                                                                                                 |
| `exclusions`           | no       |         | List of semicolon-separated (`;`) exclude patterns. Exclude patterns may contain the `*` and the `?` wildcards or a regex pattern, according to the value of the `regexp` option.                                                                        |
| `explode`              | no       | `false` | Set to `true` to extract an archive after it is deployed to Artifactory.                                                                                                                                                                                 |
| `fail-no-op`           | no       | `false` | Set to `true` if you'd like the command to return exit code 2 in case of no files are affected.                                                                                                                                                          |
| `flat`                 | no       | `false` | If set to `false`, files are uploaded according to their file system hierarchy.                                                                                                                                                                          |
| `include-dirs`         | no       | `false` | Set to `true` if you'd like to also apply the source path pattern for directories and not just for files.                                                                                                                                                |
| `insecure-tls`         | no       | `false` | Set to `true` to skip TLS certificates verification.                                                                                                                                                                                                     |
| `min-split`            | no       |         | The minimum file size in MiB required to attempt a multi-part upload. This option, as well as the functionality of multi-part upload, requires Artifactory with S3 or GCP storage.                                                                       |
| `module`               | no       |         | Optional module name for the build info. Build name and number options are mandatory when this option is provided.                                                                                                                                       |
| `password`             | no       |         | JFrog password.                                                                                                                                                                                                                                          |
| `project`              | no       |         | JFrog Artifactory project key.                                                                                                                                                                                                                           |
| `quiet`                | no       | `false` | Set to `true` to skip the sync-deletes confirmation message.                                                                                                                                                                                             |
| `recursive`            | no       | `false` | Set to `false` if you do not wish to collect artifacts in sub-folders to be uploaded to Artifactory.                                                                                                                                                     |
| `regexp`               | no       | `false` | Set to `true` to use a regular expression instead of wildcards expression to collect files to upload.                                                                                                                                                    |
| `retries`              | no       |         | Number of HTTP retries.                                                                                                                                                                                                                                  |
| `retry-wait-time`      | no       |         | Number of seconds or milliseconds to wait between retries. The numeric value should either end with s for seconds or ms for milliseconds (for example: `10s` or `100ms`).                                                                                |
| `server-id`            | no       |         | Server ID configured using the `jf config` command.                                                                                                                                                                                                      |
| `spec`                 | no       |         | Path to a File Spec.                                                                                                                                                                                                                                     |
| `spec-json`            | no       |         | Spec as JSON.                                                                                                                                                                                                                                            |
| `spec-vars`            | no       |         | List of semicolon-separated (`;`) variables in the form of `key1=value1;key2=value2;...` (wrapped by quotes) to be replaced in the File Spec. In the File Spec, the variables should be used as follows: `${key1}`.                                      |
| `split-count`          | no       |         | The maximum number of parts that can be concurrently uploaded per file during a multi-part upload. Set to `0` to disable multi-part upload. This option, as well as the functionality of multi-part upload, requires Artifactory with S3 or GCP storage. |
| `ssh-key-path`         | no       |         | SSH key file path.                                                                                                                                                                                                                                       |
| `ssh-passphrase`       | no       |         | SSH key passphrase.                                                                                                                                                                                                                                      |
| `symlinks`             | no       | `false` | Set to `true` to preserve symbolic links structure in Artifactory.                                                                                                                                                                                       |
| `sync-deletes`         | no       |         | Specific path in Artifactory, under which to sync artifacts after the upload. After the upload, this path will include only the artifacts uploaded during this upload operation. The other files under this path will be deleted.                        |
| `target-props`         | no       |         | List of semicolon-separated (`;`) properties in the form of `key1=value1;key2=value2;...`. Those properties will be attached to the uploaded artifacts.                                                                                                  |
| `threads`              | no       |         | Number of working threads.                                                                                                                                                                                                                               |
| `url`                  | no       |         | JFrog Platform URL. (example: `https://acme.jfrog.io`)                                                                                                                                                                                                   |
| `user`                 | no       |         | JFrog username.                                                                                                                                                                                                                                          |
| `shell`                | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`.                                                                                                                                                                         |

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

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-upload
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

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-upload
    with:
      source-pattern: ...
      target-pattern: ...
      spec-json: |
        {
          "files": []
        }
```
