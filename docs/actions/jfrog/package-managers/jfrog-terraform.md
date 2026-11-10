# Action `jfrog-terraform`

The [`jfrog-terraform`](../../../../.github/actions/jfrog/package-managers/jfrog-terraform/action.yml) action runs Terraform.

## Inputs

| Name           | Required | Default | Description                                                                                                                                  |
| -------------- | -------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `args`         | yes      |         | The `terraform` arguments.                                                                                                                   |
| `build-name`   | no       |         | Providing this option will collect and record build info for this build name. Build number option is mandatory when this option is provided. |
| `build-number` | no       |         | Providing this option will collect and record build info for this build number. Build name option is mandatory when this option is provided. |
| `exclusions`   | no       |         | List of semicolon-separated (`;`) exclusions. Exclusions can include the `*` and the `?` wildcards.                                          |
| `module`       | no       |         | Optional module name for the build info. Build name and number options are mandatory when this option is provided.                           |
| `namespace`    | yes      |         | Terraform namespace.                                                                                                                         |
| `project`      | no       |         | JFrog Artifactory project key.                                                                                                               |
| `provider`     | yes      |         | Terraform provider.                                                                                                                          |
| `tag`          | yes      |         | Terraform package tag.                                                                                                                       |
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

  - uses: $/.github/actions/jfrog/package-managers/jfrog-terraform
    with:
      args: ...
      namespace: ...
      provider: ...
      tag: ...
```
