# Action `jfrog-rt-transfer-plugin-install`

The [`jfrog-rt-transfer-plugin-install`](../../../../.github/actions/jfrog/rt/jfrog-rt-transfer-plugin-install/action.yml) action downloads and installs the data-transfer user plugin on the primary node of Artifactory, which is running on this local machine.

## Inputs

| Name        | Required | Default | Description                                                                      |
| ----------- | -------- | ------- | -------------------------------------------------------------------------------- |
| `server-id` | yes      |         | The ID of the source server, on which the plugin should be installed.            |
| `dir`       | no       |         | The local directory that contains the plugin files to install.                   |
| `home-dir`  | no       |         | The local JFrog home directory to install the plugin in.                         |
| `version`   | no       |         | The plugin version to download and install.                                      |
| `shell`     | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`. |

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

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-transfer-plugin-install
    with:
      server-id: ...
```
