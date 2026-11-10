# Action `jfrog-rt-ping`

The [`jfrog-rt-ping`](../../../../.github/actions/jfrog/rt/jfrog-rt-ping/action.yml) action sends applicative ping to Artifactory.

## Inputs

| Name                   | Required | Default | Description                                                                       |
| ---------------------- | -------- | ------- | --------------------------------------------------------------------------------- |
| `format`               | no       |         | Defines the output format of the command. Acceptable values are: `json`, `table`. |
| `access-token`         | no       |         | JFrog access token.                                                               |
| `client-cert-key-path` | no       |         | Private key file for the client certificate in PEM format.                        |
| `client-cert-path`     | no       |         | Client certificate file in PEM format.                                            |
| `insecure-tls`         | no       | `false` | Set to `true` to skip TLS certificates verification.                              |
| `password`             | no       |         | JFrog password.                                                                   |
| `server-id`            | no       |         | Server ID configured using the `jf config` command.                               |
| `ssh-key-path`         | no       |         | SSH key file path.                                                                |
| `ssh-passphrase`       | no       |         | SSH key passphrase.                                                               |
| `url`                  | no       |         | JFrog Platform URL. (example: `https://acme.jfrog.io`)                            |
| `user`                 | no       |         | JFrog username.                                                                   |
| `shell`                | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`.  |

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

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-ping
```
