# JFrog artifactory actions

> [!WARNING]
> The JFrog actions are **not** tested yet for the command execution. If you find any issues, please open an PR.

| Name                                                                                      | Description                                                                                                         |
| ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| [`jfrog-apk`](package-managers/jfrog-apk.md)                           | Run Alpine `apk` commands through Artifactory.                                                                      |
| [`jfrog-apt`](package-managers/jfrog-apt.md)                           | Run `apt-get` commands against a JFrog Artifactory Debian repository.                                               |
| [`jfrog-cargo`](package-managers/jfrog-cargo.md)                       | Run Cargo (Rust) commands with JFrog build info collection.                                                         |
| [`jfrog-choco`](package-managers/jfrog-choco.md)                       | Run Chocolatey with optional JFrog build info collection.                                                           |
| [`jfrog-conan`](package-managers/jfrog-conan.md)                       | Run native `conan` command.                                                                                         |
| [`jfrog-conan-config`](package-managers/jfrog-conan-config.md)         | Generate `conan` build configuration.                                                                               |
| [`jfrog-docker`](package-managers/jfrog-docker.md)                     | Run any `docker` command, including `jf docker scan` for scanning a local image with JFrog Xray.                    |
| [`jfrog-dotnet`](package-managers/jfrog-dotnet.md)                     | Run .NET Core CLI.                                                                                                  |
| [`jfrog-dotnet-config`](package-managers/jfrog-dotnet-config.md)       | Generate `dotnet` configuration.                                                                                    |
| [`jfrog-go`](package-managers/jfrog-go.md)                             | Runs `go`.                                                                                                          |
| [`jfrog-go-config`](package-managers/jfrog-go-config.md)               | Generate `go` build configuration.                                                                                  |
| [`jfrog-go-publish`](package-managers/jfrog-go-publish.md)             | Publish `go` package and/or its dependencies to Artifactory.                                                        |
| [`jfrog-gradle`](package-managers/jfrog-gradle.md)                     | Run Gradle build.                                                                                                   |
| [`jfrog-gradle-config`](package-managers/jfrog-gradle-config.md)       | Generate `gradle` build configuration.                                                                              |
| [`jfrog-helm`](package-managers/jfrog-helm.md)                         | Run native Helm command with build info collection support.                                                         |
| [`jfrog-mvn`](package-managers/jfrog-mvn.md)                           | Run Maven build.                                                                                                    |
| [`jfrog-mvn-config`](package-managers/jfrog-mvn-config.md)             | Generate `maven` build configuration.                                                                               |
| [`jfrog-mvnw`](package-managers/jfrog-mvnw.md)                         | Run a Maven build using the project's Maven Wrapper (`mvnw/mvnw.cmd`).                                              |
| [`jfrog-nix`](package-managers/jfrog-nix.md)                           | Run native `nix` commands with build info support.                                                                  |
| [`jfrog-npm`](package-managers/jfrog-npm.md)                           | Run `npm` command.                                                                                                  |
| [`jfrog-npm-config`](package-managers/jfrog-npm-config.md)             | Generate `npm` configuration.                                                                                       |
| [`jfrog-nuget`](package-managers/jfrog-nuget.md)                       | Run NuGet.                                                                                                          |
| [`jfrog-nuget-config`](package-managers/jfrog-nuget-config.md)         | Generate `nuget` configuration.                                                                                     |
| [`jfrog-pip`](package-managers/jfrog-pip.md)                           | Run `pip` install.                                                                                                  |
| [`jfrog-pip-config`](package-managers/jfrog-pip-config.md)             | Generate `pip` build configuration.                                                                                 |
| [`jfrog-pipenv`](package-managers/jfrog-pipenv.md)                     | Run `pipenv` install.                                                                                               |
| [`jfrog-pipenv-config`](package-managers/jfrog-pipenv-config.md)       | Generate `pipenv` build configuration.                                                                              |
| [`jfrog-poetry`](package-managers/jfrog-poetry.md)                     | Run `poetry` command.                                                                                               |
| [`jfrog-poetry-config`](package-managers/jfrog-poetry-config.md)       | Generate `poetry` build configuration.                                                                              |
| [`jfrog-ruby`](package-managers/jfrog-ruby.md)                         | Run native RubyGems (`gem`) and Bundler (`bundle`) commands with Artifactory authentication and build info support. |
| [`jfrog-terraform`](package-managers/jfrog-terraform.md)               | Run Terraform.                                                                                                      |
| [`jfrog-terraform-config`](package-managers/jfrog-terraform-config.md) | Generate Terraform configuration.                                                                                   |
| [`jfrog-twine`](package-managers/jfrog-twine.md)                       | Run `twine`.                                                                                                        |
| [`jfrog-yarn`](package-managers/jfrog-yarn.md)                         | Run Yarn commands.                                                                                                  |
| [`jfrog-yarn-config`](package-managers/jfrog-yarn-config.md)           | Generate Yarn configuration.                                                                                        |
