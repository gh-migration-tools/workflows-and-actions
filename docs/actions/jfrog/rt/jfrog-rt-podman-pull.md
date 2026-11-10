# Action `jfrog-rt-podman-pull`

The [`jfrog-rt-podman-pull`](../../../../.github/actions/jfrog/rt/jfrog-rt-podman-pull/action.yml) action performs Podman pull.

## Inputs

| Name             | Required | Default | Description                                                                                                                                  |
| ---------------- | -------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `image-tag`      | yes      |         | Docker image tag to pull.                                                                                                                    |
| `source-repo`    | yes      |         | Source repository in Artifactory.                                                                                                            |
| `format`         | no       |         | Defines the output format of the command. Acceptable values are: `json`, `table`.                                                            |
| `access-token`   | no       |         | JFrog access token.                                                                                                                          |
| `build-name`     | no       |         | Providing this option will collect and record build info for this build name. Build number option is mandatory when this option is provided. |
| `build-number`   | no       |         | Providing this option will collect and record build info for this build number. Build name option is mandatory when this option is provided. |
| `module`         | no       |         | Optional module name for the build info. Build name and number options are mandatory when this option is provided.                           |
| `password`       | no       |         | JFrog password.                                                                                                                              |
| `project`        | no       |         | JFrog Artifactory project key.                                                                                                               |
| `server-id`      | no       |         | Server ID configured using the `jf config` command.                                                                                          |
| `skip-login`     | no       | `false` | Set to `true` if you'd like the command to skip performing `docker login`.                                                                   |
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

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-podman-pull
    with:
      image-tag: ...
      source-repo: ...
```
