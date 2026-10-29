# Action `docker-run-windows`

The [`docker-run-windows`](../../.github/actions/docker-run-windows/action.yml) action runs a command in a Windows container.

## Inputs

| Name                | Required | Default | Description                                                                                      |
| ------------------- | -------- | ------- | ------------------------------------------------------------------------------------------------ |
| `image`             | yes      |         | Docker image name                                                                                |
| `shell`             | yes      |         | Docker image shell to run the command in.<br/> Valid values: `cmd`, `powershell`, `pwsh`, `bash` |
| `env`               | no       |         | Environment variables                                                                            |
| `mounts`            | no       |         | Docker mount specifications                                                                      |
| `working-directory` | no       |         | Working directory                                                                                |
| `command`           | yes      |         | Command to execute                                                                               |
| `debug`             | no       | `false` | Show created command                                                                             |

Supported shells:

- `cmd` (Command Prompt)
- `powershell` (Windows PowerShell 5.1)
- `pwsh` (PowerShell 7.x)
- `bash` (Git Bash)

## Outputs

| Name      | Description              |
| --------- | ------------------------ |
| `command` | The `docker run` command |

## Example

```yaml
env:
  REGISTRY: ghcr.io
  IMAGE: ghcr.io/OWNER/WINDOWS-IMAGE:TAG # Replace with the Windows container image to run.
  TOKEN: ***
steps:
  - name: Docker login
    uses: docker/login-action@v3
    with:
      registry: ${{ env.REGISTRY }}
      username: ${{ github.actor }}
      password: ${{ secrets.GITHUB_TOKEN }}

  - name: Docker pull
    shell: pwsh
    run: docker pull $env:IMAGE

  - name: Checkout repository
    uses: actions/checkout@v7.0.1

  - name: Run command
    id: run
    uses: $/.github/actions/docker-run-windows
    with:
      image: ${{ env.IMAGE }}
      shell: pwsh
      # Add optional environment variables
      env: |
        TOKEN=$env:TOKEN
        PROXY=
      # Add optional mounts
      mount: |
        type=bind,source=d:\build\artifacts,target=c:\artifacts
      command: |
        mkdir build
        ./scripts/build.ps1

  - name: Show command
    shell: pwsh
    env:
      COMMAND: ${{ steps.run.outputs.command }}
    run: Write-Output "$env:COMMAND"
```