# Creating an action at runtime

Use the `create-action` action to create an action at runtime.

 - [Documentation](../docs/actions/create-action.md)
 - [Source](../.github/actions/create-action/action.yml)

## Examples

> [!TIP]
> A working example you can find in the [`examples-create-action.yml`](../.github/workflows/examples-create-action.yml) workflow and the [workflow runs](../../../actions/workflows/examples-create-action.yml).

### With static data

Create and run an action at runtime with static data.

> [!IMPORTANT]
> Escape the `$` character used by GitHub Actions expressions with `${{ '$' }}`.
> 
> - `${{ '$' }}{{ steps.run.outputs.result }}` > `${{ steps.run.outputs.result }}`
> - `${{ '$' }}{{ inputs.salutation }}` > `${{ inputs.salutation }}`

```yaml
steps:
  - name: Create action
    uses: $/.github/actions/create-action
    with:
      name: __dynamically-created-action
      content: |
        inputs:
          salutation:
            required: true
          firstname:
            required: true
          lastname:
            required: true

        outputs:
          result:
            value: ${{ '$' }}{{ steps.run.outputs.result }}

        runs:
          using: composite
          steps:
            - name: Run
              id: run
              shell: bash
              run: |
                result="Hello ${{ '$' }}{{ inputs.salutation }} ${{ '$' }}{{ inputs.firstname }} ${{ '$' }}{{ inputs.lastname }}"
                echo "$result"
                echo "result=$result" >> "$GITHUB_OUTPUT"

  - name: Run action
    id: run
    uses: ./__dynamically-created-action
    with:
      salutation: Mr.
      firstname: John
      lastname: Doe

  - name: Show run result
    shell: bash
    env:
      RESULT: ${{ steps.run.outputs.result }}
    run: echo "result: ${RESULT}"
```

### With loaded data

Create and run an action at runtime with loaded data.

```yaml
steps:
  - name: Load action data
    id: load_action_data
    uses: $/.github/actions/load-action-data

  - name: Create action
    uses: $/.github/actions/create-action
    with:
      name: ${{ steps.load_action_data.outputs.name }}
      content: ${{ steps.load_action_data.outputs.content }}

  - name: Run action
    id: run
    uses: $/.github/actions/dynamic-action
    with:
      uses: ./${{ steps.load_action_data.outputs.name }}
      with: ${{ steps.load_action_data.outputs.inputs }}

  - name: Show run result
    shell: bash
    env:
      RESULT: ${{ fromJSON(steps.run.outputs.outputs).result }}
    run: echo "result: ${RESULT}"
```

## Remarks

> [!WARNING]
> As the action is passed as a string it will not be validated by GitHub Actions on compile-time or by [actionlint](https://github.com/rhysd/actionlint). Any errors will occour on runtime.