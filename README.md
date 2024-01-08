# github-action-workflow-samples

## Table of Contents

- [Summary](#summary)
- [References](#references)
- [How to use](#how-to-use)
  - [Perequisite](#perequisite)
  - [Run Github Action workflows](#run-github-action-workflows)

## Summary

A collection of Github Action workflow samples. For simplicity and to illustrate the concept, only manual workflow dispatch events will trigger workflows. The demonstration will not include the gitflow workflow with pull request and push request triggers involving dev, release/*, and master branches. 

## References

- [login-action Github repository](https://github.com/docker/login-action)
- [Building and testing Go](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-go)
- [Building and testing .NET](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-net)
- [Building and testing Python](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python)
- [Snyk Actions Github repository](https://github.com/snyk/actions)
- [docker-login Action Github repository](https://github.com/Azure/docker-login)
- [build-push-action Github repository](https://github.com/docker/build-push-action). This does not work with Snyk docker action for [Snyk Docker Action](https://github.com/snyk/actions/tree/master/docker)
- [CloudSmith Action Github repository](https://github.com/cloudsmith-io/action)
- [Automated versioning and package publishing using GitHub Actions](https://dotnetthoughts.net/automated-versioning-and-package-publishing-using-github-actions/)
- [Upload Go package to CloudSmith](https://help.cloudsmith.io/docs/go-registry)
- [Go -Publishing a module](https://go.dev/doc/modules/publishing)
- [Go - Module version numbering](https://go.dev/doc/modules/version-numbers)
- [Publishing on crates.io](https://doc.rust-lang.org/cargo/reference/publishing.html)

## How to use

### Perequisite

Setup a/an 

- [Azure Container registry](https://azure.microsoft.com/de-de/products/container-registry) for uploading build and tagged docker images
- [CloudSmith organization](https://cloudsmith.com/pricing) for uploading build artifacts
- [Snyk organization](https://snyk.io/de/plans/) for vulnerability scanning

### Github Action workflows

Clicking on the provided links will direct you to the respective GitHub Action workflows:

[![CI/CT workflow for C# ASP .NET Core service docker image](https://github.com/MGTheTrain/github-action-workflow-samples/actions/workflows/build_and_push_c%23_backend_service.yml/badge.svg)](https://github.com/MGTheTrain/github-action-workflow-samples/actions/workflows/build_and_push_c%23_backend_service.yml)

[![CI/CT workflow for Go Gin service docker image](https://github.com/MGTheTrain/github-action-workflow-samples/actions/workflows/build_and_push_go_backend_service.yml/badge.svg)](https://github.com/MGTheTrain/github-action-workflow-samples/actions/workflows/build_and_push_go_backend_service.yml)

[![CI/CT workflow for Python FastAPI service docker image](https://github.com/MGTheTrain/github-action-workflow-samples/actions/workflows/build_and_push_python_backend_service.yml/badge.svg)](https://github.com/MGTheTrain/github-action-workflow-samples/actions/workflows/build_and_push_python_backend_service.yml)

[![CI/CT workflow for Rust Actix Web service docker image](https://github.com/MGTheTrain/github-action-workflow-samples/actions/workflows/build_and_push_rust_backend_service.yml/badge.svg)](https://github.com/MGTheTrain/github-action-workflow-samples/actions/workflows/build_and_push_rust_backend_service.yml)

[![CI/CT workflow for C# libraries packaged via nuget](https://github.com/MGTheTrain/github-action-workflow-samples/actions/workflows/build_and_push_c%23_lib.yml/badge.svg)](https://github.com/MGTheTrain/github-action-workflow-samples/actions/workflows/build_and_push_c%23_lib.yml)

[![CI/CT workflow for packaged Go libraries](https://github.com/MGTheTrain/github-action-workflow-samples/actions/workflows/build_and_push_go_lib.yml/badge.svg)](https://github.com/MGTheTrain/github-action-workflow-samples/actions/workflows/build_and_push_go_lib.yml)

[![CI/CT workflow for Python libraries packaged via pip](https://github.com/MGTheTrain/github-action-workflow-samples/actions/workflows/build_and_push_python_lib.yml/badge.svg)](https://github.com/MGTheTrain/github-action-workflow-samples/actions/workflows/build_and_push_python_lib.yml)

[![CI/CT workflow for Rust libraries packaged via cargo](https://github.com/MGTheTrain/github-action-workflow-samples/actions/workflows/build_and_push_rust_lib.yml/badge.svg)](https://github.com/MGTheTrain/github-action-workflow-samples/actions/workflows/build_and_push_rust_lib.yml)

With correct access you can manually start one of those.
