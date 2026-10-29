# Action `dynamic-action-steps`

The [`dynamic-action-steps`](../../.github/actions/dynamic-action-steps/action.yml) action dynamically resolves and runs GitHub Actions steps.

> [!NOTE]
> This action is based on the [`dynamic-uses`](https://github.com/jenseng/dynamic-uses/blob/main/action.yml) action by [@jenseng](https://github.com/jenseng)

## Inputs

| Name           | Required | Default | Description                      |
| -------------- | :------: | ------- | -------------------------------- |
| `steps`        | yes      |         | Steps to run                     |
| `secrets_json` | no       | `{}`    | Secrets as a JSON object         |
| `debug`        | no       | `false` | Show the generated GitHub action |

## Outputs

| Name      | Description                                           |
| --------- | ------------------------------------------------------|
| `outputs` | JSON-ified outputs from the steps, keyed by step `id` |

## Examples

### With steps

```yaml
steps:
  - name: Run
    uses: $/.github/actions/dynamic-action-steps
    with:
      steps: |
        - name: Step 1
          shell: bash
          run: echo "Step 1"
        - name: Step 2
          shell: bash
          run: echo "Step 2"
        - name: Step 3
          shell: bash
          run: echo "Step 3"
```

### With nested steps

The `dynamic-action-steps` action supports the execution of actions which contain a nested `dynamic-action-steps` action call.

```yaml
steps:
  - name: Run
    uses: $/.github/actions/dynamic-action-steps
    with:
      steps: |
        - name: Nested level 1 action
          uses: $/.github/actions/dynamic-action-steps
          with:
            steps: |
              - name: Nested level 2 action
                uses: $/.github/actions/dynamic-action-steps
                with:
                  steps: |
                    - name: Nested level 3 action
                      uses: $/.github/actions/dynamic-action-steps
                      with:
                        steps: |
                          - name: Step 1
                            shell: bash
                            run: echo "Step 1"
                          - name: Step 2
                            shell: bash
                            run: echo "Step 2"
                          - name: Step 3
                            shell: bash
                            run: echo "Step 3"
```

### Use compile-time expressions

This example shows how to use expressions that are evaluated at compile-time.

- `salutation="${{ steps.variables.outputs.salutation }}"` > `salutation="Mr."`
- `firstname="${{ steps.variables.outputs.firstname }}"` > `firstname="John"`
- `lastname="${{ steps.variables.outputs.lastname }}"` > `lastname="Doe"`

```yaml
steps:
  - name: Set Variables
    id: variables
    shell: bash
    run: |
      salutation="Mr."
      firstname="John"
      lastname="Doe"

      {
        echo "salutation=$salutation"
        echo "firstname=$firstname"
        echo "lastname=$lastname"
      } >> "$GITHUB_OUTPUT"

  - name: Run
    id: run
    uses: $/.github/actions/dynamic-action-steps
    with:
      debug: true
      steps: |
        - name: Run
          id: run
          shell: bash
          run: |
            salutation="${{ steps.variables.outputs.salutation }}"
            firstname="${{ steps.variables.outputs.firstname }}"
            lastname="${{ steps.variables.outputs.lastname }}"

            sentence="Hello $salutation $firstname $lastname"

            echo "sentence=$sentence" >> "$GITHUB_OUTPUT"

  - name: Show outputs
    shell: bash
    run: echo "${{ fromJSON(steps.run.outputs.outputs).run.sentence }}"
```

> [!IMPORTANT]
> To include the outputs of a step to the `dynamic-action-steps` action outputs, the step must have an unique `id` (e.g. `id: run`).
>
> The outputs of the `dynamic-action-steps` action call are returned as a JSON string object:
> ```json
> {
>   "outputs":
>   {
>     "run":
>     {
>       "sentence": "Hello Mr. John Doe"
>     }
>   }
> }
> ```
> To access the outputs values use `${{ fromJSON(steps.run.outputs.outputs).STEP_ID.OUTPUT_NAME }}`.

### Use runtime expressions

This example shows how to use expressions that are evaluated at runtime.

- `salutation="${{ '$' }}{{ steps.variables.outputs.salutation }}"` > `salutation="${{ steps.variables.outputs.salutation }}"`
- `firstname="${{ '$' }}{{ steps.variables.outputs.firstname }}"` > `firstname="${{ steps.variables.outputs.firstname }}"`
- `lastname="${{ '$' }}{{ steps.variables.outputs.lastname }}"` > `lastname="${{ steps.variables.outputs.lastname }}"`

```yaml
steps:
  - name: Run
    id: run
    uses: $/.github/actions/dynamic-action-steps
    with:
      debug: true
      steps: |
        - name: Set Variables
          id: variables
          shell: bash
          run: |
            salutation="Mr."
            firstname="John"
            lastname="Doe"

            {
              echo "salutation=$salutation"
              echo "firstname=$firstname"
              echo "lastname=$lastname"
            } >> "$GITHUB_OUTPUT"

        - name: Run
          id: run
          shell: bash
          run: |
            salutation="${{ '$' }}{{ steps.variables.outputs.salutation }}"
            firstname="${{ '$' }}{{ steps.variables.outputs.firstname }}"
            lastname="${{ '$' }}{{ steps.variables.outputs.lastname }}"

            sentence="Hello $salutation $firstname $lastname"

            echo "sentence=$sentence" >> "$GITHUB_OUTPUT"

  - name: Show outputs
    shell: bash
    run: |
      echo "${{ fromJSON(steps.run.outputs.outputs).variables.firstname }}"
      echo "${{ fromJSON(steps.run.outputs.outputs).run.sentence }}"
```

> [!IMPORTANT]
> To include the outputs of a step to the `dynamic-action-steps` action outputs, the step must have an unique `id` (e.g. `id: run`).
>
> The outputs of the `dynamic-action-steps` action call are returned as a JSON string object:
> ```json
> {
>   "outputs":
>   {
>     "variables":
>     {
>       "salutation": "Mr.",
>       "firstname": "John",
>       "lastname": "Doe"
>     },
>     "run":
>     {
>       "sentence": "Hello Mr. John Doe"
>     }
>   }
> }
> ```
> To access the outputs values use `${{ fromJSON(steps.run.outputs.outputs).STEP_ID.OUTPUT_NAME }}`.

### Use secrets

This example shows how to pass and use secrets that are evaluated at runtime.

`secrets` **must** be passed as a JSON string object and can be accessed by `${{ '$' }}{{ fromJSON(env.SECRETS_JSON).SECRET_NAME }}`.

```yaml
steps:
  - name: Run
    uses: $/.github/actions/dynamic-action-steps
    with:
      secrets-json: ${{ toJSON(secrets) }}
      steps: |
        - name: Call API
          uses: $/.github/actions/call-api
          with:
            api-token: ${{ '$' }}{{ fromJSON(env.SECRETS_JSON).API_TOKEN }}
```

## Remarks

> [!WARNING]
> As the steps are passed as a string they will not be validated by GitHub Actions on compile-time or by [actionlint](https://github.com/rhysd/actionlint). Any errors will occour on runtime.

> [!IMPORTANT]
> Any `run` step **must have** the option `shell:` provided.