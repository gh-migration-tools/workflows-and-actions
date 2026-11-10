# Action `jfrog-rt-group-add-users`

The [`jfrog-rt-group-add-users`](../../../../.github/actions/jfrog/rt/jfrog-rt-group-add-users/action.yml) action adds a list of users to a group.

## Inputs

| Name             | Required | Default | Description                                                                      |
| ---------------- | -------- | ------- | -------------------------------------------------------------------------------- |
| `group-name`     | yes      |         | The name of the group.                                                           |
| `users-list`     | yes      |         | Specifies the usernames to add to the specified group.                           |
| `access-token`   | no       |         | JFrog access token.                                                              |
| `password`       | no       |         | JFrog password.                                                                  |
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

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-group-add-users
    with:
      group-name: ...
      users-list: ...
```
