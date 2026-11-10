# Action `jfrog-rt-permission-target-create`

The [`jfrog-rt-permission-target-create`](../../../../.github/actions/jfrog/rt/jfrog-rt-permission-target-create/action.yml) action creates a new permission target in the JFrog Platform.

## Inputs

| Name                   | Required | Default | Description                                                                                                                                                                                                       |
| ---------------------- | -------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `template-path`        | yes      |         | Specifies the local file system path for the template file to be used for the permission target creation. The template can be created using the `jf.exe rt ptt` command.                                          |
| `access-token`         | no       |         | JFrog access token.                                                                                                                                                                                               |
| `client-cert-key-path` | no       |         | Private key file for the client certificate in PEM format.                                                                                                                                                        |
| `client-cert-path`     | no       |         | Client certificate file in PEM format.                                                                                                                                                                            |
| `format`               | no       |         | Defines the output format of the command. Acceptable values are: `json`.                                                                                                                                          |
| `password`             | no       |         | JFrog password.                                                                                                                                                                                                   |
| `server-id`            | no       |         | Server ID configured using the `jf config` command.                                                                                                                                                               |
| `ssh-key-path`         | no       |         | SSH key file path.                                                                                                                                                                                                |
| `ssh-passphrase`       | no       |         | SSH key passphrase.                                                                                                                                                                                               |
| `url`                  | no       |         | JFrog Artifactory URL. (example: `https://acme.jfrog.io/artifactory`)                                                                                                                                             |
| `user`                 | no       |         | JFrog username.                                                                                                                                                                                                   |
| `vars`                 | no       |         | List of semicolon-separated (`;`) variables in the form of `key1=value1;key2=value2;...` (wrapped by quotes) to be replaced in the template. In the template, the variables should be used as follows: `${key1}`. |
| `shell`                | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`.                                                                                                                                  |

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

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-permission-target-create
    with:
      template-path: ...
```
