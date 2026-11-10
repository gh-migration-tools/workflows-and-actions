# Action `jfrog-ruby`

The [`jfrog-ruby`](../../../../.github/actions/jfrog/package-managers/jfrog-ruby/action.yml) action runs native RubyGems (`gem`) and Bundler (`bundle`) commands with Artifactory authentication and build info support.

## Inputs

| Name           | Required | Default | Description                                                                                                                                                                                                                                                                                                                                                                                               |
| -------------- | -------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tool`         | yes      |         | The name of the tool. Acceptable values are: `gem`, `bundle`.                                                                                                                                                                                                                                                                                                                                             |
| `args`         | yes      |         | The tool arguments.                                                                                                                                                                                                                                                                                                                                                                                       |
| `build-name`   | no       |         | Providing this option will collect and record build info for this build name. Build number option is mandatory when this option is provided.                                                                                                                                                                                                                                                              |
| `build-number` | no       |         | Providing this option will collect and record build info for this build number. Build name option is mandatory when this option is provided.                                                                                                                                                                                                                                                              |
| `module`       | no       |         | Optional module name for the build info. Build name and number options are mandatory when this option is provided.                                                                                                                                                                                                                                                                                        |
| `project`      | no       |         | JFrog Artifactory project key.                                                                                                                                                                                                                                                                                                                                                                            |
| `repo`         | no       |         | Specifies the Artifactory repository name for the selected package manager, replacing the interactive repository selection. The interactive selection offers virtual repositories of the matching package type, which is normally what this should be set to. Note that `gradle` matches the `gradle` package type rather than `maven`, and `pip`, `pipenv`, `poetry`, `twine` and `uv` all match `pypi`. |
| `server-id`    | no       |         | Server ID configured using the `jf config` command.                                                                                                                                                                                                                                                                                                                                                       |
| `shell`        | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`.                                                                                                                                                                                                                                                                                                                          |

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

  # Example 1
  - uses: $/.github/actions/jfrog/package-managers/jfrog-ruby
    with:
      tool: bundle
      args: install
      build-name: my-build
      build-number: 1

  # Example 2
  - uses: $/.github/actions/jfrog/package-managers/jfrog-ruby
    with:
      tool: bundle
      args: update rake
      server-id: my-rt

  # Example 3
  - uses: $/.github/actions/jfrog/package-managers/jfrog-ruby
    with:
      tool: gem
      args: install rails
      repo: gems-virtual

  # Example 4
  - uses: $/.github/actions/jfrog/package-managers/jfrog-ruby
    with:
      tool: gem
      args: install rails --source https://server/artifactory/api/gems/gems-remote/

  # Example 5
  - uses: $/.github/actions/jfrog/package-managers/jfrog-ruby
    with:
      tool: gem
      args: push my_gem-1.0.0.gem
      repo: gems-local
      build-name: my-build
      build-number: 1

  # Example 6
  - uses: $/.github/actions/jfrog/package-managers/jfrog-ruby
    with:
      tool: gem
      args: push my_gem-1.0.0.gem --host https://server/artifactory/api/gems/gems-local/
      build-name: my-build
      build-number: 1

  # Example 7
  - uses: $/.github/actions/jfrog/package-managers/jfrog-ruby
    with:
      tool: gem
      args: install rake
      repo: gems-virtual
      server-id: my-rt
```
