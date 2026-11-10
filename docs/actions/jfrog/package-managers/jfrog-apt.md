# Action `jfrog-apt`

The [`jfrog-apt`](../../../../.github/actions/jfrog/package-managers/jfrog-apt/action.yml) action runs `apt-get` commands against a JFrog Artifactory Debian repository.

## Inputs

| Name           | Required | Default | Description                                                                                                                                                                                                                                                                                                                                                                                               |
| -------------- | -------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `command`      | yes      |         | The `apt-get`/`apt-cache`/`dpkg-query` commands.                                                                                                                                                                                                                                                                                                                                                          |
| `args`         | yes      |         | The command arguments.                                                                                                                                                                                                                                                                                                                                                                                    |
| `build-name`   | no       |         | Providing this option will collect and record build info for this build name. Build number option is mandatory when this option is provided.                                                                                                                                                                                                                                                              |
| `build-number` | no       |         | Providing this option will collect and record build info for this build number. Build name option is mandatory when this option is provided.                                                                                                                                                                                                                                                              |
| `component`    | no       |         | Debian component (e.g. `main`, `contrib`, `non-free`). Multiple components: `--component "main contrib non-free"`.                                                                                                                                                                                                                                                                                        |
| `dist`         | no       |         | Debian distribution name (e.g. `noble`, `jammy`).                                                                                                                                                                                                                                                                                                                                                         |
| `module`       | no       |         | Optional module name for the build info. Build name and number options are mandatory when this option is provided.                                                                                                                                                                                                                                                                                        |
| `project`      | no       |         | JFrog Artifactory project key.                                                                                                                                                                                                                                                                                                                                                                            |
| `repo`         | no       |         | Specifies the Artifactory repository name for the selected package manager, replacing the interactive repository selection. The interactive selection offers virtual repositories of the matching package type, which is normally what this should be set to. Note that `gradle` matches the `gradle` package type rather than `maven`, and `pip`, `pipenv`, `poetry`, `twine` and `uv` all match `pypi`. |
| `server-id`    | no       |         | Server ID configured using the `jf config` command.                                                                                                                                                                                                                                                                                                                                                       |
| `skip-login`   | no       | `false` | Set to `true` if you'd like the command to skip performing login.                                                                                                                                                                                                                                                                                                                                         |
| `trusted`      | no       | `false` | Skip GPG signature verification. Use only for testing when the repository has no GPG key configured. Mutually exclusive with `--import-key`.                                                                                                                                                                                                                                                              |
| `shell`        | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`.                                                                                                                                                                                                                                                                                                                          |

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
  - uses: $/.github/actions/jfrog/package-managers/jfrog-apt
    with:
      command: install
      args: curl
      repo: ci-debian-local
      dist: bookworm

  # Example 2
  - uses: $/.github/actions/jfrog/package-managers/jfrog-apt
    with:
      command: install
      args: curl vim
      repo: ci-debian-local
      dist: bookworm
      component: main

  # Example 3
  - uses: $/.github/actions/jfrog/package-managers/jfrog-apt
    with:
      command: install
      args: curl
      skip-login: true

  # Example 4
  - uses: $/.github/actions/jfrog/package-managers/jfrog-apt
    with:
      command: install
      args: curl
      repo: ci-debian-local
      dist: bookworm
      build-name: my-build
      build-number: 1

  # Example 5
  - uses: $/.github/actions/jfrog/package-managers/jfrog-apt
    with:
      command: install
      args: curl
      repo: ci-debian-local
      dist: bookworm
      build-name: my-build
      build-number: 1
      module: debian-pkgs
      project: myproject
```
