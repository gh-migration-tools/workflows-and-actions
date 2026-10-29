# Action `dynamic-action`

The [`dynamic-action`](../../.github/actions/dynamic-action/action.yml) action dynamically resolves and runs another GitHub action.

> [!NOTE]
> This action is based on the [`dynamic-uses`](https://github.com/jenseng/dynamic-uses/blob/main/action.yml) action by [@jenseng](https://github.com/jenseng)

## Inputs

| Name           | Required | Default | Description                      |
| -------------- | :------: | ------- | -------------------------------- |
| `uses`         | yes      |         | Action reference or path         |
| `with`         | no       | `{}`    | YAML or JSON string of inputs    |
| `secrets_json` | no       | `{}`    | Secrets as a JSON object         |
| `debug`        | no       | `false` | Show the generated GitHub action |

## Outputs

| Name      | Description                        |
| --------- | ---------------------------------- |
| `outputs` | JSON-ified outputs from the action |

## Examples

### Without inputs

```yaml
steps:
  - name: Run
    uses: $/.github/actions/dynamic-action
    with:
      uses: $/.github/actions/${{ inputs.action-name }}
```

### With inputs

```yaml
steps:
  - name: Run
    id: run
    uses: $/.github/actions/dynamic-action
    with:
      uses: $/.github/actions/${{ inputs.action-name }}

      # As inline JSON inputs
      with: '{ "salutation": "Mr.", "firstname": "John", "lastname": "Doe" }'

      # As multiline JSON inputs
      with: |
        {
          "salutation": "Mr.",
          "firstname": "John",
          "lastname": "Doe"
        }

      # As YAML inputs
      with: |
        salutation: 'Mr.'
        firstname: 'John'
        lastname: 'Doe'

  - name: Show outputs
    shell: bash
    run: echo "${{ fromJSON(steps.run.outputs.outputs).sentence }}"
```

> [!IMPORTANT]
> The outputs of the `dynamic-action` action call are returned as a JSON string object:
> ```json
> {
>   "outputs":
>   {
>     "sentence": "Hello Mr. John Doe"
>   }
> }
> ```
> To access the outputs values use `${{ fromJSON(steps.run.outputs.outputs).OUTPUT_NAME }}`.

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
    uses: $/.github/actions/dynamic-action
    with:
      uses: $/.github/actions/${{ inputs.action-name }}
      with: |
        salutation: '${{ steps.variables.outputs.salutation }}'
        firstname: '${{ steps.variables.outputs.firstname }}'
        lastname: '${{ steps.variables.outputs.lastname }}'
```

### Use secrets

This example shows how to pass and use secrets that are evaluated at runtime.

`secrets` **must** be passed as a JSON string object and can be accessed by `${{ '$' }}{{ fromJSON(env.SECRETS_JSON).SECRET_NAME }}`.

```yaml
steps:
  - name: Run
    uses: $/.github/actions/dynamic-action
    with:
      secrets-json: ${{ toJSON(secrets) }}
      uses: $/.github/actions/call-api
      with: |
        api-token: ${{ '$' }}{{ fromJSON(env.SECRETS_JSON).API_TOKEN }}
```

## Remarks

> [!WARNING]
> As the inputs are passed as a string they will not be validated by GitHub Actions on compile-time or by [actionlint](https://github.com/rhysd/actionlint). Any errors will occour on runtime.