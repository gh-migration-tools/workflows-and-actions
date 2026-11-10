# Action `jfrog-rt-users-delete`

The [`jfrog-rt-users-delete`](../../../../.github/actions/jfrog/rt/jfrog-rt-users-delete/action.yml) action deletes users.

## Inputs

| Name             | Required | Default | Description                                                                                                                           |
| ---------------- | -------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `users-list`     | no       |         | Comma-separated (`,`) list of usernames to delete in the form of `user1,user2,...`.                                                   |
| `access-token`   | no       |         | JFrog access token.                                                                                                                   |
| `csv`            | no       |         | Path to a CSV file with the users' details. The first row of the file is reserved for the cells' headers. It must include `username`. |
| `password`       | no       |         | JFrog password.                                                                                                                       |
| `quiet`          | no       |         | Set to `true` to skip the delete confirmation message.                                                                                |
| `server-id`      | no       |         | Server ID configured using the `jf config` command.                                                                                   |
| `ssh-key-path`   | no       |         | SSH key file path.                                                                                                                    |
| `ssh-passphrase` | no       |         | SSH key passphrase.                                                                                                                   |
| `url`            | no       |         | JFrog Artifactory URL. (example: `https://acme.jfrog.io/artifactory`)                                                                 |
| `user`           | no       |         | JFrog username.                                                                                                                       |
| `shell`          | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`.                                                      |

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

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-users-delete
```
