# Action `jfrog-rt-build-promote`

The [`jfrog-rt-build-promote`](../../../../.github/actions/jfrog/rt/jfrog-rt-build-promote/action.yml) action promotes build in Artifactory.

## Inputs

| Name                   | Required | Default | Description                                                                                                                      |
| ---------------------- | -------- | ------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `build-name`           | yes      |         | Build name.                                                                                                                      |
| `build-number`         | yes      |         | Build number.                                                                                                                    |
| `target-repository`    | yes      |         | Build promotion target repository.                                                                                               |
| `format`               | no       |         | Defines the output format of the command. Acceptable values are: `json`.                                                         |
| `access-token`         | no       |         | JFrog access token.                                                                                                              |
| `comment`              | no       |         | Build promotion comment.                                                                                                         |
| `copy`                 | no       | `false` | If `true`, the build artifacts and dependencies are copied to the target repository, otherwise they are moved.                   |
| `dry-run`              | no       | `false` | If `true`, promotion is only simulated. The build is not promoted.                                                               |
| `fail-fast`            | no       | `false` | If `true`, fail and abort the operation upon receiving an error.                                                                 |
| `include-dependencies` | no       | `false` | If `true`, the build dependencies are also promoted.                                                                             |
| `insecure-tls`         | no       | `false` | Set to `true` to skip TLS certificates verification.                                                                             |
| `password`             | no       |         | JFrog password.                                                                                                                  |
| `project`              | no       |         | JFrog Artifactory project key.                                                                                                   |
| `props`                | no       |         | List of semicolon-separated (`;`) properties in the form of `key1=value1;key2=value2;...` to be attached to the build artifacts. |
| `server-id`            | no       |         | Server ID configured using the `jf config` command.                                                                              |
| `source-repo`          | no       |         | Build promotion source repository.                                                                                               |
| `ssh-key-path`         | no       |         | SSH key file path.                                                                                                               |
| `ssh-passphrase`       | no       |         | SSH key passphrase.                                                                                                              |
| `status`               | no       |         | Build promotion status.                                                                                                          |
| `url`                  | no       |         | JFrog Platform URL. (example: `https://acme.jfrog.io`)                                                                           |
| `user`                 | no       |         | JFrog username.                                                                                                                  |
| `shell`                | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`.                                                 |

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

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-build-promote
    with:
      build-name: ...
      build-number: ...
      target-repository: ...
```
