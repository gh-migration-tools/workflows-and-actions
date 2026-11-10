# Action `jfrog-rt-build-docker-create`

The [`jfrog-rt-build-docker-create`](../../../../.github/actions/jfrog/rt/jfrog-rt-build-docker-create/action.yml) action adds a published Docker image to the build info.

## Inputs

| Name             | Required | Default | Description                                                                                                                                  |
| ---------------- | -------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `target-repo`    | yes      |         | The repository to which the image was pushed.                                                                                                |
| `access-token`   | no       |         | JFrog access token.                                                                                                                          |
| `build-name`     | no       |         | Providing this option will collect and record build info for this build name. Build number option is mandatory when this option is provided. |
| `build-number`   | no       |         | Providing this option will collect and record build info for this build number. Build name option is mandatory when this option is provided. |
| `image-file`     | yes      |         | Path to a file which includes one line in the following format: `<IMAGE-TAG>@sha256:<MANIFEST-SHA256>`.                                      |
| `module`         | no       |         | Optional module name for the build info. Build name and number options are mandatory when this option is provided.                           |
| `password`       | no       |         | JFrog password.                                                                                                                              |
| `project`        | no       |         | JFrog Artifactory project key.                                                                                                               |
| `server-id`      | no       |         | Server ID configured using the `jf config` command.                                                                                          |
| `ssh-key-path`   | no       |         | SSH key file path.                                                                                                                           |
| `ssh-passphrase` | no       |         | SSH key passphrase.                                                                                                                          |
| `url`            | no       |         | JFrog Platform URL. (example: `https://acme.jfrog.io`)                                                                                       |
| `user`           | no       |         | JFrog username.                                                                                                                              |
| `shell`          | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`.                                                             |

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

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-build-docker-create
    with:
      target-repo: ...
      image-file: ...
```
