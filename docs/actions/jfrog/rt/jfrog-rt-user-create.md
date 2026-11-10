# Action `jfrog-rt-user-create`

The [`jfrog-rt-user-create`](../../../../.github/actions/jfrog/rt/jfrog-rt-user-create/action.yml) action creates a new user.

## Inputs

| Name             | Required | Default | Description                                                                      |
| ---------------- | -------- | ------- | -------------------------------------------------------------------------------- |
| `username`       | yes      |         | The username.                                                                    |
| `password`       | yes      |         | The password.                                                                    |
| `email`          | yes      |         | The email.                                                                       |
| `access-token`   | no       |         | JFrog access token.                                                              |
| `admin`          | no       | `false` | Set to `true` if you'd like to create an admin user.                             |
| `replace`        | no       | `false` | Set to `true` if you'd like existing users or groups to be replaced.             |
| `server-id`      | no       |         | Server ID configured using the `jf config` command.                              |
| `ssh-key-path`   | no       |         | SSH key file path.                                                               |
| `ssh-passphrase` | no       |         | SSH key passphrase.                                                              |
| `url`            | no       |         | JFrog Artifactory URL. (example: `https://acme.jfrog.io/artifactory`)            |
| `user`           | no       |         | JFrog username.                                                                  |
| `users-groups`   | no       |         | A list of comma-separated (`,`) groups for the new users to be associated with.  |
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

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-user-create
    with:
      username: ...
      password: ...
      email: ...
```
