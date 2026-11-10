# Action `jfrog-go-publish`

The [`jfrog-go-publish`](../../../../.github/actions/jfrog/package-managers/jfrog-go-publish/action.yml) action publishes `go` package and/or its dependencies to Artifactory.

## Inputs

| Name               | Required | Default | Description                                                                                                                                  |
| ------------------ | -------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `project-version`  | yes      |         | Package version to be published.                                                                                                             |
| `access-token`     | no       |         | JFrog access token.                                                                                                                          |
| `build-name`       | no       |         | Providing this option will collect and record build info for this build name. Build number option is mandatory when this option is provided. |
| `build-number`     | no       |         | Providing this option will collect and record build info for this build number. Build name option is mandatory when this option is provided. |
| `detailed-summary` | no       | `false` | Set to `true` to include a list of the affected files in the command summary.                                                                |
| `exclusions`       | no       |         | List of semicolon-separated (`;`) exclusions. Exclusions can include the `*` and the `?` wildcards.                                          |
| `module`           | no       |         | Optional module name for the build info. Build name and number options are mandatory when this option is provided.                           |
| `password`         | no       |         | JFrog password.                                                                                                                              |
| `project`          | no       |         | JFrog Artifactory project key.                                                                                                               |
| `url`              | no       |         | JFrog Artifactory URL. (example: `https://acme.jfrog.io/artifactory`)                                                                        |
| `user`             | no       |         | JFrog username.                                                                                                                              |
| `shell`            | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`.                                                             |

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

  - uses: $/.github/actions/jfrog/package-managers/jfrog-go-publish
    with:
      project-version: ...
```
