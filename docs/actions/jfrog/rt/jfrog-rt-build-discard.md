# Action `jfrog-rt-build-discard`

The [`jfrog-rt-build-discard`](../../../../.github/actions/jfrog/rt/jfrog-rt-build-discard/action.yml) action discards builds by setting retention parameters.

## Inputs

| Name               | Required | Default | Description                                                                                                                  |
| ------------------ | -------- | ------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `build-name`       | yes      |         | Build name.                                                                                                                  |
| `format`           | no       |         | Defines the output format of the command. Acceptable values are: `json`.                                                     |
| `access-token`     | no       |         | JFrog access token.                                                                                                          |
| `async`            | no       | `false` | If set to `true`, build discard will run asynchronously and will not wait for response.                                      |
| `delete-artifacts` | no       | `false` | If set to `true`, automatically removes build artifacts stored in Artifactory.                                               |
| `exclude-builds`   | no       |         | List of comma-separated (`,`) build numbers in the form of `value1,value2,...`, that should not be removed from Artifactory. |
| `insecure-tls`     | no       | `false` | Set to `true` to skip TLS certificates verification.                                                                         |
| `max-builds`       | no       |         | The maximum number of builds to store in Artifactory.                                                                        |
| `max-days`         | no       |         | The maximum number of days to keep builds in Artifactory.                                                                    |
| `password`         | no       |         | JFrog password.                                                                                                              |
| `project`          | no       |         | JFrog Artifactory project key.                                                                                               |
| `server-id`        | no       |         | Server ID configured using the `jf config` command.                                                                          |
| `ssh-key-path`     | no       |         | SSH key file path.                                                                                                           |
| `ssh-passphrase`   | no       |         | SSH key passphrase.                                                                                                          |
| `url`              | no       |         | JFrog Platform URL. (example: `https://acme.jfrog.io`)                                                                       |
| `user`             | no       |         | JFrog username.                                                                                                              |
| `shell`            | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`.                                             |

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

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-build-discard
    with:
      build-name: ...
```
