# Go

See comments in [build_and_push_go_lib.yml](../../.github/workflows/build_and_push_go_lib.yml)

Difficult setup with CloudSmith in current directory setup. See: https://help.cloudsmith.io/docs/go-registry
When working with public go modules, consider utilizing git tags as proposed here: 
- https://go.dev/doc/modules/publishing
- https://go.dev/doc/modules/version-numbers
Please, contemplate manually installing Go modules by using `go get <e.g. "github.com/MGTheTrain/github-action-workflow-samples/libraries/go/common-lib/src/domain/models">`. This action will subsequently update your `go.mod` file.