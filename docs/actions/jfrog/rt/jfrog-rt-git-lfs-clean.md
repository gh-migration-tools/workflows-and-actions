# Action `jfrog-rt-git-lfs-clean`

The [`jfrog-rt-git-lfs-clean`](../../../../.github/actions/jfrog/rt/jfrog-rt-git-lfs-clean/action.yml) action clean files from a Git LFS repository. This command deletes all files from a Git LFS repository that are no longer available in the corresponding Git repository.

## Inputs

| Name              | Required | Default | Description                                                                                                                                                               |
| ----------------- | -------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `path-to-git`     | yes      |         | Path to a directory containing the `.git` directory. If not specified, the `.git` directory is assumed to be in the current directory.                                    |
| `format`          | no       |         | Defines the output format of the command. Acceptable values are: `json`, `table`.                                                                                         |
| `access-token`    | no       |         | JFrog access token.                                                                                                                                                       |
| `dry-run`         | no       | `false` | If `true`, cleanup is only simulated. No files are actually deleted.                                                                                                      |
| `insecure-tls`    | no       | `false` | Set to `true` to skip TLS certificates verification.                                                                                                                      |
| `password`        | no       |         | JFrog password.                                                                                                                                                           |
| `quiet`           | no       | `false` | Set to `true` to skip the delete confirmation message.                                                                                                                    |
| `refs`            | no       |         | List of comma-separated (`,`) Git references in the form of `ref1,ref2,...` which should be preserved.                                                                    |
| `repo`            | no       |         | Local Git LFS repository which should be cleaned. If omitted, this is detected from the Git repository.                                                                   |
| `retries`         | no       |         | Number of HTTP retries.                                                                                                                                                   |
| `retry-wait-time` | no       |         | Number of seconds or milliseconds to wait between retries. The numeric value should either end with s for seconds or ms for milliseconds (for example: `10s` or `100ms`). |
| `server-id`       | no       |         | Server ID configured using the `jf config` command.                                                                                                                       |
| `ssh-key-path`    | no       |         | SSH key file path.                                                                                                                                                        |
| `ssh-passphrase`  | no       |         | SSH key passphrase.                                                                                                                                                       |
| `url`             | no       |         | JFrog Platform URL. (example: `https://acme.jfrog.io`)                                                                                                                    |
| `user`            | no       |         | JFrog username.                                                                                                                                                           |
| `shell`           | no       | `bash`  | Shell to use for run steps. Acceptable values are: `bash`, `powershell`, `pwsh`.                                                                                          |

## Outputs

| Name      | Description        |
| --------- | ------------------ |
| `command` | The JFrog command. |

## Example

```yaml
steps:
  - name: Setup JFrog CLI
    uses: jfrog/setup-jfrog-cli@v5.3.4
    env:
      JF_URL: ${{ vars.JF_URL }}
      JF_ACCESS_TOKEN: ${{ secrets.JF_ACCESS_TOKEN }}

  - uses: $/.github/actions/jfrog/rt/jfrog-rt-git-lfs-clean
    with:
      path-to-git: ...
```
