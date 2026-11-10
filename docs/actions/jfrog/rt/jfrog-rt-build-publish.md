# Action `jfrog-rt-build-publish`

The [`jfrog-rt-build-publish`](../../../../.github/actions/jfrog/rt/jfrog-rt-build-publish/action.yml) action publish build info.

## Inputs

| Name                   | Required | Default | Description                                                                                                                                                                                                   |
| ---------------------- | -------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `build-name`           | yes      |         | Build name.                                                                                                                                                                                                   |
| `build-number`         | yes      |         | Build number.                                                                                                                                                                                                 |
| `format`               | no       |         | Defines the output format of the command. Acceptable values are: `json`, `table`.                                                                                                                             |
| `access-token`         | no       |         | JFrog access token.                                                                                                                                                                                           |
| `build-url`            | no       |         | Can be used for setting the CI server build URL in the build info.                                                                                                                                            |
| `collect-env`          | no       | `false` | Set to `true` to collect all environment variables and add them to the build info.                                                                                                                            |
| `collect-git-info`     | no       | `false` | Set to `true` to collect Git revision and URL from the local `.git` directory and adds it to the build info.                                                                                                  |
| `dep-exclude-scopes`   | no       |         | List of semicolon-separated (`;`) dependency scopes to exclude from the published build info. Relevant for Package managers with supported dependency scopes (e.g. Maven, NPM). For example: `test;provided`. |
| `detailed-summary`     | no       | `false` | Set to `true` to get a command summary with details about the build info artifact.                                                                                                                            |
| `dot-git-path`         | no       |         | Path to the `.git` directory. If not provided, the `.git` directory will be searched in the current working directory or its parent directories. Only respected when `collect-git-info` is enabled.           |
| `dry-run`              | no       | `false` | Set to `true` to get a preview of the recorded build info, without publishing it to Artifactory.                                                                                                              |
| `env-exclude`          | no       |         | List of case insensitive patterns in the form of `value1;value2;...`. Environment variables match those patterns will be excluded.                                                                            |
| `env-include`          | no       |         | List of patterns in the form of `value1;value2;...`. Only environment variables match those patterns will be included.                                                                                        |
| `git-config-file-path` | no       |         | Path to the `git` configuration file. Only respected when `collect-git-info` is enabled.                                                                                                                      |
| `insecure-tls`         | no       | `false` | Set to `true` to skip TLS certificates verification.                                                                                                                                                          |
| `overwrite`            | no       | `false` | Overwrites all existing occurrences of build infos with the provided name and number. Build artifacts will not be deleted.                                                                                    |
| `password`             | no       |         | JFrog password.                                                                                                                                                                                               |
| `project`              | no       |         | JFrog Artifactory project key.                                                                                                                                                                                |
| `server-id`            | no       |         | Server ID configured using the `jf config` command.                                                                                                                                                           |
| `ssh-key-path`         | no       |         | SSH key file path.                                                                                                                                                                                            |
| `ssh-passphrase`       | no       |         | SSH key passphrase.                                                                                                                                                                                           |
| `url`                  | no       |         | JFrog Platform URL. (example: `https://acme.jfrog.io`)                                                                                                                                                        |
| `user`                 | no       |         | JFrog username.                                                                                                                                                                                               |
| `shell`                | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`.                                                                                                                              |

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

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-build-publish
    with:
      build-name: ...
      build-number: ...
```
