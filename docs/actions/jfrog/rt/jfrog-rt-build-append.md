# Action `jfrog-rt-build-append`

The [`jfrog-rt-build-append`](../../../../.github/actions/jfrog/rt/jfrog-rt-build-append/action.yml) action appends published build to the build info.

## Inputs

| Name                     | Required | Default | Description                                                                                                                        |
| ------------------------ | -------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `build-name`             | yes      |         | The current build name.                                                                                                            |
| `build-number`           | yes      |         | The current build number.                                                                                                          |
| `build-name-to-append`   | yes      |         | The published build name to append to the current build.                                                                           |
| `build-number-to-append` | yes      |         | The published build number to append to the current build.                                                                         |
| `access-token`           | no       |         | JFrog access token.                                                                                                                |
| `build-url`              | no       |         | Can be used for setting the CI server build URL in the build info.                                                                 |
| `dry-run`                | no       | `false` | Set to `true` to get a preview of the recorded build info, without publishing it to Artifactory.                                   |
| `env-exclude`            | no       |         | List of case insensitive patterns in the form of `value1;value2;...`. Environment variables match those patterns will be excluded. |
| `env-include`            | no       |         | List of patterns in the form of `value1;value2;...`. Only environment variables match those patterns will be included.             |
| `insecure-tls`           | no       | `false` | Set to `true` to skip TLS certificates verification.                                                                               |
| `password`               | no       |         | JFrog password.                                                                                                                    |
| `project`                | no       |         | JFrog Artifactory project key.                                                                                                     |
| `server-id`              | no       |         | Server ID configured using the `jf config` command.                                                                                |
| `ssh-key-path`           | no       |         | SSH key file path.                                                                                                                 |
| `ssh-passphrase`         | no       |         | SSH key passphrase.                                                                                                                |
| `url`                    | no       |         | JFrog Platform URL. (example: `https://acme.jfrog.io`)                                                                             |
| `user`                   | no       |         | JFrog username.                                                                                                                    |
| `shell`                  | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`.                                                   |

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

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-build-append
    with:
      build-name: ...
      build-number: ...
      build-name-to-append: ...
      build-number-to-append: ...
```
