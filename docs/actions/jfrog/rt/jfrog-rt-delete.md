# Action `jfrog-rt-delete`

The [`jfrog-rt-delete`](../../../../.github/actions/jfrog/rt/jfrog-rt-delete/action.yml) action deletes files from Artifactory.

## Inputs

| Name                   | Required | Default | Description                                                                                                                                                                                                                                                                                                                 |
| ---------------------- | -------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `delete-pattern`       | yes      |         | Specifies the source path in Artifactory, from which the artifacts should be deleted, in the following format: `<repository name>/<repository path>`. You can use wildcards to specify multiple artifacts.                                                                                                                  |
| `format`               | no       |         | Defines the output format of the command. Acceptable values are: `json`, `table`.                                                                                                                                                                                                                                           |
| `access-token`         | no       |         | JFrog access token.                                                                                                                                                                                                                                                                                                         |
| `archive-entries`      | no       |         | This option is no longer supported since version `7.90.5` of Artifactory. If specified, only archive artifacts containing entries matching this pattern are matched. You can use wildcards to specify multiple artifacts.                                                                                                   |
| `build`                | no       |         | If specified, only artifacts of the specified build are matched. The property format is `build-name/build-number`. If you do not specify the build number, the artifacts are filtered by the latest build number. If the build is assigned to a specific project please provide the project key using the `--project` flag. |
| `client-cert-key-path` | no       |         | Private key file for the client certificate in PEM format.                                                                                                                                                                                                                                                                  |
| `client-cert-path`     | no       |         | Client certificate file in PEM format.                                                                                                                                                                                                                                                                                      |
| `dry-run`              | no       | `false` | Set to `true` to disable communication with Artifactory.                                                                                                                                                                                                                                                                    |
| `exclude-artifacts`    | no       |         | If specified, build artifacts are not matched. Used together with the `--build` flag.                                                                                                                                                                                                                                       |
| `exclude-props`        | no       |         | List of semicolon-separated (`;`) properties in the form of `key1=value1;key2=value2;...`. Only artifacts without the specified properties will be deleted.                                                                                                                                                                 |
| `exclusions`           | no       |         | List of semicolon-separated (`;`) exclusions. Exclusions can include the `*` and the `?` wildcards.                                                                                                                                                                                                                         |
| `fail-no-op`           | no       | `false` | Set to `true` if you'd like the command to return exit code 2 in case of no files are affected.                                                                                                                                                                                                                             |
| `include-deps`         | no       |         | If specified, also dependencies of the specified build are matched. Used together with the `--build` flag.                                                                                                                                                                                                                  |
| `insecure-tls`         | no       | `false` | Set to `true` to skip TLS certificates verification.                                                                                                                                                                                                                                                                        |
| `limit`                | no       |         | The maximum number of items to fetch. Usually used with the `sort-by` option.                                                                                                                                                                                                                                               |
| `offset`               | no       |         | The offset from which to fetch items (i.e. how many items should be skipped). Usually used with the `sort-by` option.                                                                                                                                                                                                       |
| `password`             | no       |         | JFrog password.                                                                                                                                                                                                                                                                                                             |
| `project`              | no       |         | JFrog Artifactory project key.                                                                                                                                                                                                                                                                                              |
| `props`                | no       |         | List of semicolon-separated (`;`) properties in the form of `key1=value1;key2=value2;...`. Only artifacts with these properties will be deleted.                                                                                                                                                                            |
| `quiet`                | no       | `false` | Set to `true` to skip the delete confirmation message.                                                                                                                                                                                                                                                                      |
| `recursive`            | no       | `false` | Set to `false` if you do not wish to delete artifacts inside sub-folders in Artifactory.                                                                                                                                                                                                                                    |
| `retries`              | no       |         | Number of HTTP retries.                                                                                                                                                                                                                                                                                                     |
| `retry-wait-time`      | no       |         | Number of seconds or milliseconds to wait between retries. The numeric value should either end with s for seconds or ms for milliseconds (for example: `10s` or `100ms`).                                                                                                                                                   |
| `server-id`            | no       |         | Server ID configured using the `jf config` command.                                                                                                                                                                                                                                                                         |
| `sort-by`              | no       |         | List of semicolon-separated (`;`) fields to sort by. The fields must be part of the `items` AQL domain.                                                                                                                                                                                                                     |
| `sort-order`           | no       |         | The order by which fields in the `sort-by` option should be sorted. Accepts `asc` or `desc`.                                                                                                                                                                                                                                |
| `spec`                 | no       |         | Path to a File Spec.                                                                                                                                                                                                                                                                                                        |
| `spec-json`            | no       |         | Spec as JSON.                                                                                                                                                                                                                                                                                                               |
| `spec-vars`            | no       |         | List of semicolon-separated (`;`) variables in the form of `key1=value1;key2=value2;...` (wrapped by quotes) to be replaced in the File Spec. In the File Spec, the variables should be used as follows: `${key1}`.                                                                                                         |
| `ssh-key-path`         | no       |         | SSH key file path.                                                                                                                                                                                                                                                                                                          |
| `ssh-passphrase`       | no       |         | SSH key passphrase.                                                                                                                                                                                                                                                                                                         |
| `threads`              | no       |         | Number of working threads.                                                                                                                                                                                                                                                                                                  |
| `url`                  | no       |         | JFrog Platform URL. (example: `https://acme.jfrog.io`)                                                                                                                                                                                                                                                                      |
| `user`                 | no       |         | JFrog username.                                                                                                                                                                                                                                                                                                             |
| `shell`                | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`.                                                                                                                                                                                                                                            |

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

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-delete
    with:
      delete-pattern: ...
```

### With spec JSON

```yaml
steps:
  - name: Setup JFrog CLI
    uses: jfrog/setup-jfrog-cli@v5.3.4
    env:
      JF_URL: ${{ vars.JF_URL }}
      JF_ACCESS_TOKEN: ${{ secrets.JF_ACCESS_TOKEN }}

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-delete
    with:
      delete-pattern: ...
      spec-json: |
        {
          "files": []
        }
```
