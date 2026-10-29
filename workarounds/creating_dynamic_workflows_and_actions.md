# Creating dynamic workflows and actions

GitHub Actions **do not** support the creation of dynamic workflows and actions in comparison to Azure Pipelines (`stepList`) or GitLab (`before_script`/`after_script`).

To get around this limitation use the `dynamic-action-steps` action.

- [Documentation](../docs/actions/dynamic-action-steps.md)
- [Source](../.github/actions/dynamic-action-steps/action.yml)

## Example workflow

> [!TIP]
> A working example you can find in the [`examples-run-dynamic-workflow.yml`](../.github/workflows/examples-run-dynamic-workflow.yml) workflow and the [workflow runs](../../../actions/workflows/examples-run-dynamic-workflow.yml).

### Create dynamic workflow

Create a dynamic workflow with the `workflow_call` event and optional `pre-build-steps`/`post-build-steps` inputs.

```yaml
on:
  workflow_call:
    inputs:
      pre-build-steps:
        description: Pre-build steps
        type: string
        required: false
        default: ''
      post-build-steps:
        description: Post-build steps
        type: string
        required: false
        default: ''

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Pre-build steps
        uses: $/.github/actions/dynamic-action-steps
        if: ${{ inputs.pre-build-steps != '' }}
        with:
          steps: ${{ inputs.pre-build-steps }}

      - name: Build
        run: ...

      - name: Post-build steps
        uses: $/.github/actions/dynamic-action-steps
        if: ${{ inputs.post-build-steps != '' }}
        with:
          steps: ${{ inputs.post-build-steps }}
```

### Run dynamic workflow

Run the dynamic workflow in another workflow and pass steps as string to the `pre-build-steps`/`post-build-steps` inputs.

```yaml
on:
  workflow_dispatch:

jobs:
  build:
    uses: $/.github/workflows/build.yml
    with:
      pre-build-steps: |
        - name: Run pre-build step 1
          shell: bash
          run: ...
        - name: Run pre-build step 2
          shell: bash
          run: ...
      post-build-steps: |
        - name: Run post-build step 1
          shell: bash
          run: ...
        - name: Run post-build step 2
          shell: bash
          run: ...
```

## Example action

> [!TIP]
> A working example you can find in the [`examples-run-dynamic-action.yml`](../.github/workflows/examples-run-dynamic-action.yml) workflow and the [workflow runs](../../../actions/workflows/examples-run-dynamic-action.yml).

### Create dynamic action

Create a dynamic action with optional `pre-build-steps`/`post-build-steps` inputs.

```yaml
name: Build
description: Build

inputs:
  pre-build-steps:
    description: Pre-build steps
    required: false
    default: ''
  post-build-steps:
    description: Post-build steps
    required: false
    default: ''

runs:
  using: composite
  steps:
    - name: Pre-build steps
      uses: $/.github/actions/dynamic-action-steps
      if: ${{ inputs.pre-build-steps != '' }}
      with:
        steps: ${{ inputs.pre-build-steps }}

    - name: Build
      shell: bash
      run: ...

    - name: Post-build steps
      uses: $/.github/actions/dynamic-action-steps
      if: ${{ inputs.post-build-steps != '' }}
      with:
        steps: ${{ inputs.post-build-steps }}
```

### Run dynamic action

Run the dynamic action in a workflow or action and pass steps as string to the `pre-build-steps`/`post-build-steps` inputs.

```yaml
on:
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Build
        uses: $/.github/actions/build
        with:
          pre-build-steps: |
            - name: Run pre-build step 1
              shell: bash
              run: ...
            - name: Run pre-build step 2
              shell: bash
              run: ...
          post-build-steps: |
            - name: Run post-build step 1
              shell: bash
              run: ...
            - name: Run post-build step 2
              shell: bash
              run: ...
```

## Remarks

> [!WARNING]
> As the steps are passed as a string they will not be validated by GitHub Actions on compile-time or by [actionlint](https://github.com/rhysd/actionlint). Any errors will occour on runtime.

> [!IMPORTANT]
> Any `run` step **must have** the option `shell:` provided.