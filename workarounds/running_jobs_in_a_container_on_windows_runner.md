# Running jobs in a container on Windows runner

GitHub Actions **do not** support running jobs in a container on Windows runners, this is only supported by Linux runners.

### ❌ Running jobs in a container

```yaml
jobs:
  build:
    runs-on: windows-latest
    container:
      image: hello-world
```

For workflows that require Windows containers, use the Docker CLI or the `docker-run-windows` action.

- [Documentation](../docs/actions/docker-run-windows.md)
- [Source](../.github/actions/docker-run-windows/action.yml)

## Examples

### With Docker CLI

Use the Docker CLI to run commands in a Windows container using a shell installed on the image.

```yaml
jobs:
  build:
    runs-on: windows-latest
    env:
      REGISTRY: ghcr.io
      IMAGE: ghcr.io/OWNER/WINDOWS-IMAGE:TAG
      DIR_GITHUB_WORKSPACE: C:\github_workspace
      DIR_RUNNER_TEMP: C:\runner_temp
    steps:
      # Ommit the login step if the image do not require authentication
      - name: Docker login
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      # Pull the Docker image
      - name: Docker pull
        shell: pwsh
        run: docker pull "${IMAGE}"

      - name: Checkout repository
        uses: actions/checkout@v7.0.1

      # Run a command in a Docker container
      - name: Docker run
        shell: pwsh
        run: |
          $command = @'
            mkdir build
            ./scripts/build.ps1
          '@

          # Concatenates the multiline command into one-line command
          $command = ($command -split '\r?\n' | Where-Object { -not [string]::IsNullOrWhiteSpace($_.Trim()) }) -join '; '

          docker run `
            --env "GITHUB_WORKSPACE=$env:DIR_GITHUB_WORKSPACE" `
            --env "RUNNER_TEMP=$env:DIR_RUNNER_TEMP" `
            --mount "type=bind,source=$env:GITHUB_WORKSPACE,target=$env:DIR_GITHUB_WORKSPACE" `
            --mount "type=bind,source=$env:RUNNER_TEMP,target=$env:DIR_RUNNER_TEMP" `
            --workdir "$env:DIR_GITHUB_WORKSPACE" `
            "$env:IMAGE" `
            pwsh.exe -NoLogo -NoProfile -Command $command
```

### With action

Use the `docker-run-windows` action to run commands in a Windows container using a shell installed on the image. The action supports the shells:

- `cmd` (Command Prompt)
- `powershell` (Windows PowerShell 5.1)
- `pwsh` (PowerShell 7.x)
- `bash` (Git Bash)

```yaml
- name: Run command
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
```

## Remarks

> [!NOTE]
> - Unlike the Linux `container` job option, this approach does not automatically pass the host's environment variables into the container. Pass any required variables explicitly with the `-e|--env` option or `env:` input.
> - Mount the directories whose contents you need to keep, such as the workspace, temporary or build artifacts directory. Otherwise, files created only inside the container will be lost when it stops.

> [!TIP]
> An example for installing additional shells on a Windows image can be found in this [Dockerfile](../tests/docker/Dockerfile).