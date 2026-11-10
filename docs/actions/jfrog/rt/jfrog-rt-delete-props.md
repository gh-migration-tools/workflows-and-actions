# Action `jfrog-rt-delete-props`

The [`jfrog-rt-delete-props`](../../../../.github/actions/jfrog/rt/jfrog-rt-delete-props/action.yml) action deletes properties on existing files in Artifactory.

## Inputs

| Name                   | Required | Default | Description                                                                                                                                                                                                                                                                                                                 |
| ---------------------- | -------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `files-pattern`        | yes      |         | Properties of artifacts that match this pattern will be removed. In the following format: `<repository name>/<repository path>`. You can use wildcards to specify multiple artifacts.                                                                                                                                       |
| `properties-list`      | yes      |         | List of comma-separated (`,`) properties, in the form of `key1,key2,...`, to be removed from the matching files.                                                                                                                                                                                                            |
| `format`               | no       |         | Defines the output format of the command. Acceptable values are: `json`, `table`.                                                                                                                                                                                                                                           |
| `access-token`         | no       |         | JFrog access token.                                                                                                                                                                                                                                                                                                         |
| `archive-entries`      | no       |         | This option is no longer supported since version `7.90.5` of Artifactory. If specified, only archive artifacts containing entries matching this pattern are matched. You can use wildcards to specify multiple artifacts.                                                                                                   |
| `build`                | no       |         | If specified, only artifacts of the specified build are matched. The property format is `build-name/build-number`. If you do not specify the build number, the artifacts are filtered by the latest build number. If the build is assigned to a specific project please provide the project key using the `--project` flag. |
| `bundle`               | no       |         | If specified, only artifacts of the specified bundle are matched. The value format is `bundle-name/bundle-version`.                                                                                                                                                                                                         |
| `client-cert-key-path` | no       |         | Private key file for the client certificate in PEM format.                                                                                                                                                                                                                                                                  |
| `client-cert-path`     | no       |         | Client certificate file in PEM format.                                                                                                                                                                                                                                                                                      |
| `exclude-artifacts`    | no       |         | If specified, build artifacts are not matched. Used together with the `--build` flag.                                                                                                                                                                                                                                       |
| `exclude-props`        | no       |         | List of semicolon-separated (`;`) properties in the form of `key1=value1;key2=value2;...`. Only artifacts without the specified properties are affected.                                                                                                                                                                    |
| `exclusions`           | no       |         | List of semicolon-separated (`;`) exclusions. Exclusions can include the `*` and the `?` wildcards.                                                                                                                                                                                                                         |
| `fail-no-op`           | no       | `false` | Set to `true` if you'd like the command to return exit code 2 in case of no files are affected.                                                                                                                                                                                                                             |
| `include-deps`         | no       |         | If specified, also dependencies of the specified build are matched. Used together with the `--build` flag.                                                                                                                                                                                                                  |
| `include-dirs`         | no       | `false` | Set to `true` if you'd like to also apply the source path pattern for directories and not just for files.                                                                                                                                                                                                                   |
| `insecure-tls`         | no       | `false` | Set to `true` to skip TLS certificates verification.                                                                                                                                                                                                                                                                        |
| `limit`                | no       |         | The maximum number of items to fetch. Usually used with the `sort-by` option.                                                                                                                                                                                                                                               |
| `offset`               | no       |         | The offset from which to fetch items (i.e. how many items should be skipped). Usually used with the `sort-by` option.                                                                                                                                                                                                       |
| `password`             | no       |         | JFrog password.                                                                                                                                                                                                                                                                                                             |
| `project`              | no       |         | JFrog Artifactory project key.                                                                                                                                                                                                                                                                                              |
| `props`                | no       |         | List of semicolon-separated (`;`) properties in the form of `key1=value1;key2=value2;...`. Only artifacts with these properties are affected.                                                                                                                                                                               |
| `recursive`            | no       | `false` | When `false`, artifacts inside sub-folders in Artifactory will not be affected.                                                                                                                                                                                                                                             |
| `repo-only`            | no       | `false` | When `true`, properties will be applicable only on repository level.                                                                                                                                                                                                                                                        |
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

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-delete-props
    with:
      files-pattern: ...
      properties-list: ...
```

### With spec JSON

```yaml
steps:
  - name: Setup JFrog CLI
    uses: jfrog/setup-jfrog-cli@v5.3.4
    env:
      JF_URL: ${{ vars.JF_URL }}
      JF_ACCESS_TOKEN: ${{ secrets.JF_ACCESS_TOKEN }}

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-delete-props
    with:
      files-pattern: ...
      properties-list: ...
      spec-json: |
        {
          "files": []
        }
```
