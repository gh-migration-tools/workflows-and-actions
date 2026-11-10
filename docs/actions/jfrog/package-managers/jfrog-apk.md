# Action `jfrog-apk`

The [`jfrog-apk`](../../../../.github/actions/jfrog/package-managers/jfrog-apk/action.yml) action runs Alpine `apk` commands through Artifactory, with build info collection for `add`, `upgrade`, and `upload`.

## Inputs

| Name             | Required | Default | Description                                                                                                                                                                                                                                                                                                                                                                                               |
| ---------------- | -------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `subcommand`     | yes      |         | The `apk` subcommand.                                                                                                                                                                                                                                                                                                                                                                                     |
| `alpine-version` | no       |         | Alpine release version, e.g. `v3.20`. Used by upload (required) and to select the Artifactory path for other subcommands.                                                                                                                                                                                                                                                                                 |
| `arch`           | no       |         | CPU architecture override (`x86_64`, `aarch64`, `armhf`, ...). Inferred from the `.apk` filename by default.                                                                                                                                                                                                                                                                                              |
| `branch`         | no       |         | Alpine repository branch to upload into, e.g. `main` or `community`.                                                                                                                                                                                                                                                                                                                                      |
| `build-name`     | no       |         | Providing this option will collect and record build info for this build name. Build number option is mandatory when this option is provided.                                                                                                                                                                                                                                                              |
| `build-number`   | no       |         | Providing this option will collect and record build info for this build number. Build name option is mandatory when this option is provided.                                                                                                                                                                                                                                                              |
| `module`         | no       |         | Optional module name for the build info. Build name and number options are mandatory when this option is provided.                                                                                                                                                                                                                                                                                        |
| `password`       | no       |         | JFrog password.                                                                                                                                                                                                                                                                                                                                                                                           |
| `project`        | no       |         | JFrog Artifactory project key.                                                                                                                                                                                                                                                                                                                                                                            |
| `repo`           | no       |         | Specifies the Artifactory repository name for the selected package manager, replacing the interactive repository selection. The interactive selection offers virtual repositories of the matching package type, which is normally what this should be set to. Note that `gradle` matches the `gradle` package type rather than `maven`, and `pip`, `pipenv`, `poetry`, `twine` and `uv` all match `pypi`. |
| `server-id`      | no       |         | Server ID configured using the `jf config` command.                                                                                                                                                                                                                                                                                                                                                       |
| `user`           | no       |         | JFrog username.                                                                                                                                                                                                                                                                                                                                                                                           |
| `shell`          | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`.                                                                                                                                                                                                                                                                                                                          |

## Outputs

| Name      | Description        |
| --------- | ------------------ |
| `command` | The JFrog command. |

## Examples

```yaml
steps:
  - name: Setup JFrog CLI
    uses: jfrog/setup-jfrog-cli@v5.3.4
    env:
      JF_URL: ${{ vars.JF_URL }}
      JF_ACCESS_TOKEN: ${{ secrets.JF_ACCESS_TOKEN }}

  # Example 1
  - uses: $/.github/actions/jfrog/package-managers/jfrog-apk
    with:
      subcommand: add curl bash
      build-name: ci-image
      build-number: 42

  # Example 2
  - uses: $/.github/actions/jfrog/package-managers/jfrog-apk
    with:
      subcommand: upgrade
      server-id: my-server
      repo: my-alpine-repo

  # Example 3
  - uses: $/.github/actions/jfrog/package-managers/jfrog-apk
    with:
      subcommand: upload ./myapp-1.0.0-r0.x86_64.apk
      repo: my-alpine-repo
      alpine-version: v3.20
      build-name: ci-image
      build-number: 42

  # Example 4
  - uses: $/.github/actions/jfrog/package-managers/jfrog-apk
    with:
      subcommand: update

  # Example 5
  - uses: $/.github/actions/jfrog/package-managers/jfrog-apk
    with:
      subcommand: search curl

  # Example 6
  - uses: $/.github/actions/jfrog/package-managers/jfrog-apk
    with:
      subcommand: info musl
```
