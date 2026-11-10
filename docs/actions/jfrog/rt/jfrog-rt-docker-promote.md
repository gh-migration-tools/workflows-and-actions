# Action `jfrog-rt-docker-promote`

The [`jfrog-rt-docker-promote`](../../../../.github/actions/jfrog/rt/jfrog-rt-docker-promote/action.yml) action promotes a Docker image from one repository to another. Supported by local repositories only.

## Inputs

| Name                  | Required | Default | Description                                                                                |
| --------------------- | -------- | ------- | ------------------------------------------------------------------------------------------ |
| `source-docker-image` | yes      |         | The docker image name to promote.                                                          |
| `source-repo`         | yes      |         | Source repository in Artifactory.                                                          |
| `target-repo`         | yes      |         | Target repository in Artifactory.                                                          |
| `format`              | no       |         | Defines the output format of the command. Acceptable values are: `json`.                   |
| `access-token`        | no       |         | JFrog access token.                                                                        |
| `copy`                | no       | `false` | If set `true`, the Docker image is copied to the target repository, otherwise it is moved. |
| `password`            | no       |         | JFrog password.                                                                            |
| `server-id`           | no       |         | Server ID configured using the `jf config` command.                                        |
| `source-tag`          | no       |         | The tag name to promote.                                                                   |
| `ssh-key-path`        | no       |         | SSH key file path.                                                                         |
| `ssh-passphrase`      | no       |         | SSH key passphrase.                                                                        |
| `target-docker-image` | no       |         | Docker target image name.                                                                  |
| `target-tag`          | no       |         | The target tag to assign the image after promotion.                                        |
| `url`                 | no       |         | JFrog Platform URL. (example: `https://acme.jfrog.io`)                                     |
| `user`                | no       |         | JFrog username.                                                                            |
| `shell`               | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`.           |

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

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-docker-promote
    with:
      source-docker-image: ...
      source-repo: ...
      target-repo: ...
```
