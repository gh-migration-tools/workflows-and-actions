# Running actions with dynamic name

GitHub Actions **do not** support running workflows and actions with dynamic name, as the `uses` path must be a static string in order for GitHub Actions to resolve the dependency graph.

To get around this limitation use the `dynamic-action` action (see [example](#-dynamic-action-name)).

- [Documentation](../docs/actions/dynamic-action.md)
- [Source](../.github/actions/dynamic-action/action.yml)

### ❌ Dynamic workflow name

```yaml
on:
  workflow_dispatch:
    inputs:
      os:
        description: os
        type: choice
        default: linux
        options:
          - linux
          - windows

jobs:
  build:
    uses: $/.github/workflows/build-${{ inputs.os }}.yml
```

### ❌ Dynamic action name

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        os:
          - linux
          - windows
    steps:
      - uses: $/.github/actions/build-${{ matrix.os }}
```

## Examples

### ✅ Dynamic workflow name

There is **actual no** workaround to run a workflow with dynamic name. The only solution is to create separate jobs with an `if` statement for each workflow.

```yaml
on:
  workflow_dispatch:
    inputs:
      os:
        description: os
        type: choice
        default: linux
        options:
          - linux
          - windows
jobs:
  build-linux:
    uses: $/.github/workflows/build-linux.yml
    if: ${{ inputs.os == 'linux' }}

  build-windows:
    uses: $/.github/workflows/build-windows.yml
    if: ${{ inputs.os == 'windows' }}
```

### ✅ Dynamic action name

Use the `dynamic-action` action to run an action with dynamic name.

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        os:
          - linux
          - windows
    steps:
      - name: Build
        uses: $/.github/actions/dynamic-action
        with:
          uses: $/.github/actions/build-${{ matrix.os }}
          with: |
            input1: 'value1'
            input2: 'value2'
```

## Remarks

> [!WARNING]
> As the inputs are passed as a string they will not be validated by GitHub Actions on compile-time or by [actionlint](https://github.com/rhysd/actionlint). Any errors will occour on runtime.