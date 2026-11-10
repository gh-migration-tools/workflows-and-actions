# Action `jfrog-helm`

The [`jfrog-helm`](../../../../.github/actions/jfrog/package-managers/jfrog-helm/action.yml) action runs native Helm command with build info collection support.

## Inputs

| Name           | Required | Default | Description                                                                                                                                  |
| -------------- | -------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `args`         | yes      |         | Helm command and arguments to execute. All standard Helm commands are supported.                                                             |
| `build-name`   | no       |         | Providing this option will collect and record build info for this build name. Build number option is mandatory when this option is provided. |
| `build-number` | no       |         | Providing this option will collect and record build info for this build number. Build name option is mandatory when this option is provided. |
| `module`       | no       |         | Optional module name for the build info. Build name and number options are mandatory when this option is provided.                           |
| `password`     | no       |         | JFrog password.                                                                                                                              |
| `project`      | no       |         | JFrog Artifactory project key.                                                                                                               |
| `server-id`    | no       |         | Server ID configured using the `jf config` command.                                                                                          |
| `username`     | no       |         | Docker registry username.                                                                                                                    |
| `shell`        | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`.                                                             |

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
  - uses: $/.github/actions/jfrog/package-managers/jfrog-helm
    with:
      args: push mychart-0.1.0.tgz oci://myrepo.jfrog.io/helm-local
      build-name: my-build
      build-number: 1

  # Example 2
  - uses: $/.github/actions/jfrog/package-managers/jfrog-helm
    with:
      args: package ./mychart
      build-name: my-build
      build-number: 1

  # Example 3
  - uses: $/.github/actions/jfrog/package-managers/jfrog-helm
    with:
      args: dependency update ./mychart
      build-name: my-build
      build-number: 1

  # Example 4
  - uses: $/.github/actions/jfrog/package-managers/jfrog-helm
    with:
      args: package .
      build-name: my-build
      build-number: 1
      server-id: my-server
```
