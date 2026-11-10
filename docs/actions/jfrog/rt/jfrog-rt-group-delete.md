# Action `jfrog-rt-group-delete`

The [`jfrog-rt-group-delete`](../../../../.github/actions/jfrog/rt/jfrog-rt-group-delete/action.yml) action deletes a user group.

## Inputs

| Name             | Required | Default | Description                                                                      |
| ---------------- | -------- | ------- | -------------------------------------------------------------------------------- |
| `group-name`     | yes      |         | Group name to be deleted.                                                        |
| `access-token`   | no       |         | JFrog access token.                                                              |
| `password`       | no       |         | JFrog password.                                                                  |
| `quiet`          | no       |         | Set to `true` to skip the delete confirmation message.                           |
| `server-id`      | no       |         | Server ID configured using the `jf config` command.                              |
| `ssh-key-path`   | no       |         | SSH key file path.                                                               |
| `ssh-passphrase` | no       |         | SSH key passphrase.                                                              |
| `url`            | no       |         | JFrog Artifactory URL. (example: `https://acme.jfrog.io/artifactory`)            |
| `user`           | no       |         | JFrog username.                                                                  |
| `shell`          | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`. |

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

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-group-delete
    with:
      group-name: ...
```
