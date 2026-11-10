# Workflows and actions

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/gh-migration-tools/workflows-and-actions/actions/workflows/tests.yml/badge.svg)](https://github.com/gh-migration-tools/workflows-and-actions/actions/workflows/tests.yml)

This repository provides reusable GitHub Actions workflows and actions.

## Workarounds

- [Calling workflows with dedicated run](workarounds/calling_workflows_with_dedicated_run.md)
- [Creating an action at runtime](workarounds/creating_an_action_at_runtime.md)
- [Creating dynamic workflows and actions](workarounds/creating_dynamic_workflows_and_actions.md)
- [Running actions with dynamic name](workarounds/running_actions_with_dynamic_name.md)
- [Running jobs in a container on Windows runner](workarounds/running_jobs_in_a_container_on_windows_runner.md)

## Common actions/workflows

### Actions

| Name                                                                  | Description                                                                                 |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| [`create-action`](docs/actions/common/create-action.md)               | Creates an action at runtime                                                                |
| [`dispatch-workflow`](docs/actions/common/dispatch-workflow.md)       | Dispatches a `workflow_dispatch` workflow run in a repository and polls it until completion |
| [`docker-run-windows`](docs/actions/common/docker-run-windows.md)     | Runs a command in a Windows container                                                       |
| [`dynamic-action`](docs/actions/common/dynamic-action.md)             | Dynamically resolves and runs another GitHub action                                         |
| [`dynamic-action-steps`](docs/actions/common/dynamic-action-steps.md) | Dynamically resolves and runs GitHub Actions steps                                          |

### Workflows

| Name                                                       | Description                                                                                 |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| [`dispatch-workflow`](docs/workflows/dispatch-workflow.md) | Dispatches a `workflow_dispatch` workflow run in a repository and polls it until completion |

## JFrog

> [!WARNING]
> The JFrog actions are **not** tested yet for the command execution. If you find any issues, please open an PR.

### JFrog Artifactory actions

| Name                                                                                                  | Description                                                                                                                     |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| [`jfrog-rt-build-add-dependencies`](docs/actions/jfrog/rt/jfrog-rt-build-add-dependencies.md)         | Adds dependencies from the local file-system to the build info.                                                                 |
| [`jfrog-rt-build-add-git`](docs/actions/jfrog/rt/jfrog-rt-build-add-git.md)                           | Collects the Git revision and URL from the local `.git` directory and adds it to the build info.                                |
| [`jfrog-rt-build-append`](docs/actions/jfrog/rt/jfrog-rt-build-append.md)                             | Append published build to the build info.                                                                                       |
| [`jfrog-rt-build-clean`](docs/actions/jfrog/rt/jfrog-rt-build-clean.md)                               | Cleans (removes) build info collected locally.                                                                                  |
| [`jfrog-rt-build-collect-env`](docs/actions/jfrog/rt/jfrog-rt-build-collect-env.md)                   | Collect environment variables. Environment variables can be excluded using the `build-publish` command.                         |
| [`jfrog-rt-build-discard`](docs/actions/jfrog/rt/jfrog-rt-build-discard.md)                           | Discard builds by setting retention parameters.                                                                                 |
| [`jfrog-rt-build-docker-create`](docs/actions/jfrog/rt/jfrog-rt-build-docker-create.md)               | Add a published Docker image to the build info.                                                                                 |
| [`jfrog-rt-build-promote`](docs/actions/jfrog/rt/jfrog-rt-build-promote.md)                           | Promotes build in Artifactory.                                                                                                  |
| [`jfrog-rt-build-publish`](docs/actions/jfrog/rt/jfrog-rt-build-publish.md)                           | Publish build info.                                                                                                             |
| [`jfrog-rt-copy`](docs/actions/jfrog/rt/jfrog-rt-copy.md)                                             | Copy files between Artifactory paths.                                                                                           |
| [`jfrog-rt-curl`](docs/actions/jfrog/rt/jfrog-rt-curl.md)                                             | Execute a cURL command, using the configured Artifactory details.                                                               |
| [`jfrog-rt-delete`](docs/actions/jfrog/rt/jfrog-rt-delete.md)                                         | Delete files from Artifactory.                                                                                                  |
| [`jfrog-rt-delete-props`](docs/actions/jfrog/rt/jfrog-rt-delete-props.md)                             | Delete properties on existing files in Artifactory.                                                                             |
| [`jfrog-rt-direct-download`](docs/actions/jfrog/rt/jfrog-rt-direct-download.md)                       | Download files using direct API respecting Artifactory's native resolution order and bypassing AQL.                             |
| [`jfrog-rt-docker-promote`](docs/actions/jfrog/rt/jfrog-rt-docker-promote.md)                         | Promotes a Docker image from one repository to another.                                                                         |
| [`jfrog-rt-download`](docs/actions/jfrog/rt/jfrog-rt-download.md)                                     | Download files from Artifactory to local file system.                                                                           |
| [`jfrog-rt-git-lfs-clean`](docs/actions/jfrog/rt/jfrog-rt-git-lfs-clean.md)                           | Clean files from a Git LFS repository.                                                                                          |
| [`jfrog-rt-group-add-users`](docs/actions/jfrog/rt/jfrog-rt-group-add-users.md)                       | Add a list of users to a group.                                                                                                 |
| [`jfrog-rt-group-create`](docs/actions/jfrog/rt/jfrog-rt-group-create.md)                             | Create a new user group                                                                                                         |
| [`jfrog-rt-group-delete`](docs/actions/jfrog/rt/jfrog-rt-group-delete.md)                             | Delete a user group                                                                                                             |
| [`jfrog-rt-move`](docs/actions/jfrog/rt/jfrog-rt-move.md)                                             | Move files between Artifactory paths.                                                                                           |
| [`jfrog-rt-nuget-deps-tree`](docs/actions/jfrog/rt/jfrog-rt-nuget-deps-tree.md)                       | Show solution dependency tree.                                                                                                  |
| [`jfrog-rt-permission-target-create`](docs/actions/jfrog/rt/jfrog-rt-permission-target-create.md)     | Create a new permission target in the JFrog Platform.                                                                           |
| [`jfrog-rt-permission-target-delete`](docs/actions/jfrog/rt/jfrog-rt-permission-target-delete.md)     | Permanently delete a permission target.                                                                                         |
| [`jfrog-rt-permission-target-template`](docs/actions/jfrog/rt/jfrog-rt-permission-target-template.md) | Create a JSON template for a permission target creation or replacement.                                                         |
| [`jfrog-rt-permission-target-update`](docs/actions/jfrog/rt/jfrog-rt-permission-target-update.md)     | Update a permission target in the JFrog Platform.                                                                               |
| [`jfrog-rt-ping`](docs/actions/jfrog/rt/jfrog-rt-ping.md)                                             | Send applicative ping to Artifactory.                                                                                           |
| [`jfrog-rt-podman-pull`](docs/actions/jfrog/rt/jfrog-rt-podman-pull.md)                               | Podman pull.                                                                                                                    |
| [`jfrog-rt-podman-push`](docs/actions/jfrog/rt/jfrog-rt-podman-push.md)                               | Podman push.                                                                                                                    |
| [`jfrog-rt-replication-create`](docs/actions/jfrog/rt/jfrog-rt-replication-create.md)                 | Create a new replication in Artifactory.                                                                                        |
| [`jfrog-rt-replication-delete`](docs/actions/jfrog/rt/jfrog-rt-replication-delete.md)                 | Remove a replication repository from Artifactory.                                                                               |
| [`jfrog-rt-replication-template`](docs/actions/jfrog/rt/jfrog-rt-replication-template.md)             | Create a JSON template for creating a replication repository.                                                                   |
| [`jfrog-rt-repo-create`](docs/actions/jfrog/rt/jfrog-rt-repo-create.md)                               | Create a new repository in Artifactory.                                                                                         |
| [`jfrog-rt-repo-delete`](docs/actions/jfrog/rt/jfrog-rt-repo-delete.md)                               | Permanently delete repositories with all of their content from Artifactory.                                                     |
| [`jfrog-rt-repo-template`](docs/actions/jfrog/rt/jfrog-rt-repo-template.md)                           | Create a JSON template for repository creation or update.                                                                       |
| [`jfrog-rt-repo-update`](docs/actions/jfrog/rt/jfrog-rt-repo-update.md)                               | Update an existing repository configuration in Artifactory.                                                                     |
| [`jfrog-rt-search`](docs/actions/jfrog/rt/jfrog-rt-search.md)                                         | Search files in Artifactory.                                                                                                    |
| [`jfrog-rt-set-props`](docs/actions/jfrog/rt/jfrog-rt-set-props.md)                                   | Set properties on existing files in Artifactory.                                                                                |
| [`jfrog-rt-transfer-config`](docs/actions/jfrog/rt/jfrog-rt-transfer-config.md)                       | Copy the full configuration from a source Artifactory server to a target server                                                 |
| [`jfrog-rt-transfer-config-merge`](docs/actions/jfrog/rt/jfrog-rt-transfer-config-merge.md)           | Merge projects and repositories from a source Artifactory instance to a target Artifactory instance, if no conflicts are found. |
| [`jfrog-rt-transfer-files`](docs/actions/jfrog/rt/jfrog-rt-transfer-files.md)                         | Transfer files from one Artifactory to another.                                                                                 |
| [`jfrog-rt-transfer-plugin-install`](docs/actions/jfrog/rt/jfrog-rt-transfer-plugin-install.md)       | Download and install the data-transfer user plugin on the primary node of Artifactory, which is running on this local machine.  |
| [`jfrog-rt-transfer-settings`](docs/actions/jfrog/rt/jfrog-rt-transfer-settings.md)                   | Configure the settings for the `jf rt transfer-files` command.                                                                  |
| [`jfrog-rt-upload`](docs/actions/jfrog/rt/jfrog-rt-upload.md)                                         | Upload files from local file system to Artifactory.                                                                             |
| [`jfrog-rt-user-create`](docs/actions/jfrog/rt/jfrog-rt-user-create.md)                               | Create a new user.                                                                                                              |
| [`jfrog-rt-users-create`](docs/actions/jfrog/rt/jfrog-rt-users-create.md)                             | Create new users.                                                                                                               |
| [`jfrog-rt-users-delete`](docs/actions/jfrog/rt/jfrog-rt-users-delete.md)                             | Delete users.                                                                                                                   |

### JFrog package manager actions

| Name                                                                                      | Description                                                                                                         |
| ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| [`jfrog-apk`](docs/actions/jfrog/package-managers/jfrog-apk.md)                           | Run Alpine `apk` commands through Artifactory.                                                                      |
| [`jfrog-apt`](docs/actions/jfrog/package-managers/jfrog-apt.md)                           | Run `apt-get` commands against a JFrog Artifactory Debian repository.                                               |
| [`jfrog-cargo`](docs/actions/jfrog/package-managers/jfrog-cargo.md)                       | Run Cargo (Rust) commands with JFrog build info collection.                                                         |
| [`jfrog-choco`](docs/actions/jfrog/package-managers/jfrog-choco.md)                       | Run Chocolatey with optional JFrog build info collection.                                                           |
| [`jfrog-conan`](docs/actions/jfrog/package-managers/jfrog-conan.md)                       | Run native `conan` command.                                                                                         |
| [`jfrog-conan-config`](docs/actions/jfrog/package-managers/jfrog-conan-config.md)         | Generate `conan` build configuration.                                                                               |
| [`jfrog-docker`](docs/actions/jfrog/package-managers/jfrog-docker.md)                     | Run any `docker` command, including `jf docker scan` for scanning a local image with JFrog Xray.                    |
| [`jfrog-dotnet`](docs/actions/jfrog/package-managers/jfrog-dotnet.md)                     | Run .NET Core CLI.                                                                                                  |
| [`jfrog-dotnet-config`](docs/actions/jfrog/package-managers/jfrog-dotnet-config.md)       | Generate `dotnet` configuration.                                                                                    |
| [`jfrog-go`](docs/actions/jfrog/package-managers/jfrog-go.md)                             | Runs `go`.                                                                                                          |
| [`jfrog-go-config`](docs/actions/jfrog/package-managers/jfrog-go-config.md)               | Generate `go` build configuration.                                                                                  |
| [`jfrog-go-publish`](docs/actions/jfrog/package-managers/jfrog-go-publish.md)             | Publish `go` package and/or its dependencies to Artifactory.                                                        |
| [`jfrog-gradle`](docs/actions/jfrog/package-managers/jfrog-gradle.md)                     | Run Gradle build.                                                                                                   |
| [`jfrog-gradle-config`](docs/actions/jfrog/package-managers/jfrog-gradle-config.md)       | Generate `gradle` build configuration.                                                                              |
| [`jfrog-helm`](docs/actions/jfrog/package-managers/jfrog-helm.md)                         | Run native Helm command with build info collection support.                                                         |
| [`jfrog-mvn`](docs/actions/jfrog/package-managers/jfrog-mvn.md)                           | Run Maven build.                                                                                                    |
| [`jfrog-mvn-config`](docs/actions/jfrog/package-managers/jfrog-mvn-config.md)             | Generate `maven` build configuration.                                                                               |
| [`jfrog-mvnw`](docs/actions/jfrog/package-managers/jfrog-mvnw.md)                         | Run a Maven build using the project's Maven Wrapper (`mvnw/mvnw.cmd`).                                              |
| [`jfrog-nix`](docs/actions/jfrog/package-managers/jfrog-nix.md)                           | Run native `nix` commands with build info support.                                                                  |
| [`jfrog-npm`](docs/actions/jfrog/package-managers/jfrog-npm.md)                           | Run `npm` command.                                                                                                  |
| [`jfrog-npm-config`](docs/actions/jfrog/package-managers/jfrog-npm-config.md)             | Generate `npm` configuration.                                                                                       |
| [`jfrog-nuget`](docs/actions/jfrog/package-managers/jfrog-nuget.md)                       | Run NuGet.                                                                                                          |
| [`jfrog-nuget-config`](docs/actions/jfrog/package-managers/jfrog-nuget-config.md)         | Generate `nuget` configuration.                                                                                     |
| [`jfrog-pip`](docs/actions/jfrog/package-managers/jfrog-pip.md)                           | Run `pip` install.                                                                                                  |
| [`jfrog-pip-config`](docs/actions/jfrog/package-managers/jfrog-pip-config.md)             | Generate `pip` build configuration.                                                                                 |
| [`jfrog-pipenv`](docs/actions/jfrog/package-managers/jfrog-pipenv.md)                     | Run `pipenv` install.                                                                                               |
| [`jfrog-pipenv-config`](docs/actions/jfrog/package-managers/jfrog-pipenv-config.md)       | Generate `pipenv` build configuration.                                                                              |
| [`jfrog-poetry`](docs/actions/jfrog/package-managers/jfrog-poetry.md)                     | Run `poetry` command.                                                                                               |
| [`jfrog-poetry-config`](docs/actions/jfrog/package-managers/jfrog-poetry-config.md)       | Generate `poetry` build configuration.                                                                              |
| [`jfrog-ruby`](docs/actions/jfrog/package-managers/jfrog-ruby.md)                         | Run native RubyGems (`gem`) and Bundler (`bundle`) commands with Artifactory authentication and build info support. |
| [`jfrog-terraform`](docs/actions/jfrog/package-managers/jfrog-terraform.md)               | Run Terraform.                                                                                                      |
| [`jfrog-terraform-config`](docs/actions/jfrog/package-managers/jfrog-terraform-config.md) | Generate Terraform configuration.                                                                                   |
| [`jfrog-twine`](docs/actions/jfrog/package-managers/jfrog-twine.md)                       | Run `twine`.                                                                                                        |
| [`jfrog-yarn`](docs/actions/jfrog/package-managers/jfrog-yarn.md)                         | Run Yarn commands.                                                                                                  |
| [`jfrog-yarn-config`](docs/actions/jfrog/package-managers/jfrog-yarn-config.md)           | Generate Yarn configuration.                                                                                        |
