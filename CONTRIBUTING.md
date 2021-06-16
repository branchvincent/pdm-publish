# Contributing

Before getting started, install [Poetry](https://python-poetry.org/docs/#installation).

## Getting Started

To install the project:

```sh
poetry install
```

Optionally, you can also install [pre-commit](https://pre-commit.com/) hooks:

```sh
poetry run pre-commit install
```

Lastly, to see common tasks with [taskipy](https://github.com/illBeRoy/taskipy):

```sh
poetry run task --list
```

## Linting

To ensure code quality, we use the following tools:

- Formatting: [black](https://black.readthedocs.io/en/stable/) and [isort](https://isort.readthedocs.io/en/latest/)
- Linting: [flake8](http://flake8.pycqa.org/en/latest/)
- Type checking: [mypy](https://mypy.readthedocs.io/en/stable/)

To run these:

```sh
poetry run task lint
```

## Testing

To run tests via [pytest](https://docs.pytest.org/en/latest/):

```sh
poetry run test
```

## Releasing

Releasing is fully automated via our [CI pipeline](.github/workflows/ci.yaml). On each commit to `main`, it will:

1. Lint and test the codebase
1. Determine if a new version should be released (using [conventional commits](https://www.conventionalcommits.org/))
1. If so, bump the version and publish a new release

To override this behavior, include `[cd skip]` in your commit message.
