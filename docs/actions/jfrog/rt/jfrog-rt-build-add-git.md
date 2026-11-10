# Action `jfrog-rt-build-add-git`

The [`jfrog-rt-build-add-git`](../../../../.github/actions/jfrog/rt/jfrog-rt-build-add-git/action.yml) action collects the Git revision and URL from the local `.git` directory and adds it to the build info.

## Inputs

| Name           | Required | Default | Description                                                                                                                                                                |
| -------------- | -------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `build-name`   | yes      |         | Build name.                                                                                                                                                                |
| `build-number` | yes      |         | Build number.                                                                                                                                                              |
| `path-to-git`  | yes      |         | Path to a directory containing the `.git` directory. If not specified, the `.git` directory is assumed to be in the current directory or in one of the parent directories. |
| `config`       | no       |         | Path to a configuration file.                                                                                                                                              |
| `project`      | no       |         | JFrog Artifactory project key.                                                                                                                                             |
| `server-id`    | no       |         | Server ID configured using the `jf config` command.                                                                                                                        |
| `shell`        | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`.                                                                                           |

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

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-build-add-git
    with:
      build-name: ...
      build-number: ...
      path-to-git: ...
```
