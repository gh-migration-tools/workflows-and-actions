# escape=`
FROM mcr.microsoft.com/windows/servercore:ltsc2025

ARG POWERSHELL_VERSION=latest
ARG GIT_VERSION=latest

SHELL ["powershell.exe", "-NoLogo", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", "$ErrorActionPreference = 'Stop'; $ProgressPreference = 'SilentlyContinue';"]

RUN $headers = @{ 'User-Agent' = 'windows-shells-image' }; `
    $releasePath = if ($env:POWERSHELL_VERSION -eq 'latest') { 'latest' } else { 'tags/v' + $env:POWERSHELL_VERSION }; `
    $release = Invoke-RestMethod -Headers $headers -Uri ('https://api.github.com/repos/PowerShell/PowerShell/releases/' + $releasePath); `
    $asset = @($release.assets | Where-Object { $_.name -like 'PowerShell-7.*-win-x64.zip' }); `
    if ($asset.Count -ne 1) { throw 'Expected one PowerShell 7 Windows x64 ZIP asset.' }; `
    Invoke-WebRequest -UseBasicParsing -Uri $asset[0].browser_download_url -OutFile C:\powershell.zip; `
    Expand-Archive -Path C:\powershell.zip -DestinationPath C:\PowerShell; `
    Remove-Item C:\powershell.zip

RUN $headers = @{ 'User-Agent' = 'windows-shells-image' }; `
    $releasePath = if ($env:GIT_VERSION -eq 'latest') { 'latest' } else { 'tags/v' + $env:GIT_VERSION }; `
    $release = Invoke-RestMethod -Headers $headers -Uri ('https://api.github.com/repos/git-for-windows/git/releases/' + $releasePath); `
    $asset = @($release.assets | Where-Object { $_.name -like 'Git-*-64-bit.exe' }); `
    if ($asset.Count -ne 1) { throw 'Expected one Git for Windows x64 installer asset.' }; `
    Invoke-WebRequest -UseBasicParsing -Uri $asset[0].browser_download_url -OutFile C:\git-setup.exe; `
    $installer = Start-Process -FilePath C:\git-setup.exe -ArgumentList '/VERYSILENT', '/NORESTART', '/NOCANCEL', '/SP-', '/SUPPRESSMSGBOXES', '/DIR=C:\Git' -Wait -PassThru; `
    if ($installer.ExitCode -ne 0) { throw ('Git installation failed with exit code ' + $installer.ExitCode) }; `
    Remove-Item C:\git-setup.exe

ENV PATH="C:\PowerShell;C:\Git\bin;C:\Git\cmd;C:\Windows\System32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0"

SHELL ["cmd.exe", "/D", "/S", "/C"]

RUN powershell.exe -NoLogo -NoProfile -Command "if ($PSVersionTable.PSVersion.ToString() -notlike '5.1.*') { exit 1 }; $PSVersionTable.PSVersion" && `
    pwsh.exe -NoLogo -NoProfile -Command "if ($PSVersionTable.PSVersion.Major -ne 7) { exit 1 }; $PSVersionTable.PSVersion" && `
    bash.exe --noprofile --norc -c "exit 0" && `
    bash.exe --version

CMD ["pwsh.exe", "-NoLogo", "-NoProfile"]