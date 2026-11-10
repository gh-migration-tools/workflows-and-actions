# Action `jfrog-rt-replication-delete`

The [`jfrog-rt-replication-delete`](../../../../.github/actions/jfrog/rt/jfrog-rt-replication-delete/action.yml) action removes a replication repository from Artifactory.

## Inputs

| Name                   | Required | Default | Description                                                                      |
| ---------------------- | -------- | ------- | -------------------------------------------------------------------------------- |
| `repository-key`       | yes      |         | The repository from which the replication will be deleted.                       |
| `access-token`         | no       |         | JFrog access token.                                                              |
| `client-cert-key-path` | no       |         | Private key file for the client certificate in PEM format.                       |
| `client-cert-path`     | no       |         | Client certificate file in PEM format.                                           |
| `password`             | no       |         | JFrog password.                                                                  |
| `quiet`                | no       | `false` | Set to `true` to skip the delete confirmation message.                           |
| `server-id`            | no       |         | Server ID configured using the `jf config` command.                              |
| `ssh-key-path`         | no       |         | SSH key file path.                                                               |
| `ssh-passphrase`       | no       |         | SSH key passphrase.                                                              |
| `url`                  | no       |         | JFrog Platform URL. (example: `https://acme.jfrog.io`)                           |
| `user`                 | no       |         | JFrog username.                                                                  |
| `shell`                | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`. |

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

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-replication-delete
    with:
      repository-key: ...
```
