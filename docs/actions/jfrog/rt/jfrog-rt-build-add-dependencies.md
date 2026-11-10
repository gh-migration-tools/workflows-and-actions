# Action `jfrog-rt-build-add-dependencies`

The [`jfrog-rt-build-add-dependencies`](../../../../.github/actions/jfrog/rt/jfrog-rt-build-add-dependencies/action.yml) action adds dependencies from the local file-system to the build info.

## Inputs

| Name           | Required | Default | Description                                                                                                                                                                                                         |
| -------------- | -------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `build-name`   | yes      |         | Build name.                                                                                                                                                                                                         |
| `build-number` | yes      |         | Build number.                                                                                                                                                                                                       |
| `pattern`      | yes      |         | Without the `--from-rt` option, this argument specifies the local file system.                                                                                                                                      |
| `format`       | no       |         | Defines the output format of the command. Acceptable values are: `json`, `table`.                                                                                                                                   |
| `dry-run`      | no       | `false` | Set to `true` to only get a summary of the dependencies that will be added to the build info.                                                                                                                       |
| `exclusions`   | no       |         | List of semicolon-separated (`;`) exclude patterns. Exclude patterns may contain the `*` and the `?` wildcards or a regex pattern, according to the value of the `regexp` option.                                   |
| `from-rt`      | no       | `false` | Set `true` to search the files in Artifactory, rather than on the local file system. The `--regexp` option is not supported when `--from-rt` is set to `true`.                                                      |
| `module`       | no       |         | Optional module name in the build info for adding the dependency.                                                                                                                                                   |
| `project`      | no       |         | JFrog Artifactory project key.                                                                                                                                                                                      |
| `recursive`    | no       | `false` | Set to `false` if you do not wish to collect artifacts in sub-folders to be added to the build info.                                                                                                                |
| `regexp`       | no       | `false` | Set to `true` to use a regular expression instead of wildcards expression to collect files to be added to the build info.                                                                                           |
| `server-id`    | no       |         | Server ID configured using the `jf config` command.                                                                                                                                                                 |
| `spec`         | no       |         | Path to a File Spec.                                                                                                                                                                                                |
| `spec-json`    | no       |         | Spec as JSON.                                                                                                                                                                                                       |
| `spec-vars`    | no       |         | List of semicolon-separated (`;`) variables in the form of `key1=value1;key2=value2;...` (wrapped by quotes) to be replaced in the File Spec. In the File Spec, the variables should be used as follows: `${key1}`. |
| `shell`        | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`.                                                                                                                                    |

## Outputs

| Name      | Description        |
| --------- | ------------------ |
| `command` | The JFrog command. |

## Examples

### Basic

```yaml
steps:
  - name: Setup JFrog CLI
    uses: jfrog/setup-jfrog-cli@v5.3.4
    env:
      JF_URL: ${{ vars.JF_URL }}
      JF_ACCESS_TOKEN: ${{ secrets.JF_ACCESS_TOKEN }}

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-build-add-dependencies
    with:
      build-name: ...
      build-number: ...
      pattern: ...
```

### With spec JSON

```yaml
steps:
  - name: Setup JFrog CLI
    uses: jfrog/setup-jfrog-cli@v5.3.4
    env:
      JF_URL: ${{ vars.JF_URL }}
      JF_ACCESS_TOKEN: ${{ secrets.JF_ACCESS_TOKEN }}

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-build-add-dependencies
    with:
      build-name: ...
      build-number: ...
      pattern: ...
      spec-json: |
        {
          "files": []
        }
```
