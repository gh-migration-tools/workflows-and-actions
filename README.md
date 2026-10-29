# Workflows and actions

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/gh-migration-tools/workflows-and-actions/actions/workflows/tests.yml/badge.svg)](https://github.com/gh-migration-tools/workflows-and-actions/actions/workflows/tests.yml)

This repository provides reusable GitHub Actions workflows and actions.

## Documentation

### Actions

| Name                                                           | Description |
| -------------------------------------------------------------- | ----------- |
| [`create-action`](docs/actions/create-action.md)               | Creates an action at runtime |
| [`dispatch-workflow`](docs/actions/dispatch-workflow.md)       | Dispatches a `workflow_dispatch` workflow run in a repository and polls it until completion |
| [`docker-run-windows`](docs/actions/docker-run-windows.md)     | Runs a command in a Windows container |
| [`dynamic-action`](docs/actions/dynamic-action.md)             | Dynamically resolves and runs another GitHub action |
| [`dynamic-action-steps`](docs/actions/dynamic-action-steps.md) | Dynamically resolves and runs GitHub Actions steps |

### Workflows

| Name                                                       | Description |
| ---------------------------------------------------------- | ----------- |
| [`dispatch-workflow`](docs/workflows/dispatch-workflow.md) | Dispatches a `workflow_dispatch` workflow run in a repository and polls it until completion |

## Workarounds

- [Calling workflows with dedicated run](workarounds/calling_workflows_with_dedicated_run.md)
- [Creating an action at runtime](workarounds/creating_an_action_at_runtime.md)
- [Creating dynamic workflows and actions](workarounds/creating_dynamic_workflows_and_actions.md)
- [Running actions with dynamic name](workarounds/running_actions_with_dynamic_name.md)
- [Running jobs in a container on Windows runner](workarounds/running_jobs_in_a_container_on_windows_runner.md)