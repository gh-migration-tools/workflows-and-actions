# Action `jfrog-yarn`

The [`jfrog-yarn`](../../../../.github/actions/jfrog/package-managers/jfrog-yarn/action.yml) action runs Yarn commands.

## Inputs

| Name           | Required | Default | Description                                                                                                                                  |
| -------------- | -------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `command`      | no       |         | The `yarn` command.                                                                                                                          |
| `build-name`   | no       |         | Providing this option will collect and record build info for this build name. Build number option is mandatory when this option is provided. |
| `build-number` | no       |         | Providing this option will collect and record build info for this build number. Build name option is mandatory when this option is provided. |
| `module`       | no       |         | Optional module name for the build info. Build name and number options are mandatory when this option is provided.                           |
| `project`      | no       |         | JFrog Artifactory project key.                                                                                                               |
| `server-id`    | no       |         | Server ID configured using the `jf config` command. Supported from yarn v4+ in native mode (`JFROG_RUN_NATIVE=true`).                        |
| `shell`        | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`.                                                             |

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

  - uses: $/.github/actions/jfrog/package-managers/jfrog-yarn
    with:
      command: <caller-supplied-yarn-command>
      build-name: <caller-supplied-build-name>
      build-number: <caller-supplied-build-number>
```
