# Action `jfrog-rt-curl`

The [`jfrog-rt-curl`](../../../../.github/actions/jfrog/rt/jfrog-rt-curl/action.yml) action executes a cURL command, using the configured Artifactory details.

## Inputs

| Name           | Required | Default | Description                                                                      |
| -------------- | -------- | ------- | -------------------------------------------------------------------------------- |
| `curl-command` | yes      |         | cURL command to run.                                                             |
| `server-id`    | no       |         | Server ID configured using the `jf config` command.                              |
| `shell`        | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`. |

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

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-curl
    with:
      curl-command: ...
```
