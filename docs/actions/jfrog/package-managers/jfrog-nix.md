# Action `jfrog-nix`

The [`jfrog-nix`](../../../../.github/actions/jfrog/package-managers/jfrog-nix/action.yml) action runs native `nix` commands with build info support.

## Inputs

| Name           | Required | Default | Description                                                                                                                                  |
| -------------- | -------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `command`      | yes      |         | Wraps native Nix commands (`nix-channel`, `nix-env`, `nix-build`, `nix copy`).                                                               |
| `args`         | yes      |         | The command arguments.                                                                                                                       |
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

  # Example 1
  - uses: $/.github/actions/jfrog/package-managers/jfrog-nix
    with:
      command: nix-channel
      args:  --add https://server/artifactory/api/nix/repo/channels/nixos-25.11 nixpkgs

  # Example 2
  - uses: $/.github/actions/jfrog/package-managers/jfrog-nix
    with:
      command: nix-channel
      args:  --update

  # Example 3
  - uses: $/.github/actions/jfrog/package-managers/jfrog-nix
    with:
      command: nix-env
      args: -iA nixpkgs.hello
      build-name: my-build
      build-number: 1

  # Example 4
  - uses: $/.github/actions/jfrog/package-managers/jfrog-nix
    with:
      command: nix-build
      args: '<nixpkgs>' -A hello
      build-name: my-build
      build-number: 1

  # Example 5
  - uses: $/.github/actions/jfrog/package-managers/jfrog-nix
    with:
      command: copy
      args: --to "http://user:pass@server/artifactory/api/nix/repo/" ./result
      build-name: my-build
      build-number: 1
```
