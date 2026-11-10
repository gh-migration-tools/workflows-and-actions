# Action `jfrog-cargo`

The [`jfrog-cargo`](../../../../.github/actions/jfrog/package-managers/jfrog-cargo/action.yml) action runs Cargo (Rust) commands with JFrog build info collection.

## Inputs

| Name           | Required | Default | Description                                                                                                                                  |
| -------------- | -------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `subcommand`   | yes      |         | Cargo subcommand and its native flags.                                                                                                       |
| `build-name`   | no       |         | Providing this option will collect and record build info for this build name. Build number option is mandatory when this option is provided. |
| `build-number` | no       |         | Providing this option will collect and record build info for this build number. Build name option is mandatory when this option is provided. |
| `module`       | no       |         | Optional module name for the build info. Build name and number options are mandatory when this option is provided.                           |
| `project`      | no       |         | JFrog Artifactory project key.                                                                                                               |
| `server-id`    | no       |         | Server ID configured using the `jf config` command.                                                                                          |
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

  - uses: $/.github/actions/jfrog/package-managers/jfrog-cargo
    with:
      subcommand: ...
```
