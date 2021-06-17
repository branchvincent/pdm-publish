# PDM Publish

[![ci](https://github.com/branchvincent/pdm-publish/workflows/CI/badge.svg)](https://github.com/branchvincent/pdm-publish/actions/workflows/ci.yaml)
[![pypi version](https://img.shields.io/pypi/v/pdm-publish.svg)](https://pypi.org/project/pdm-publish/)
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

A PDM plugin to publish to PyPI

> NOTE: Consider if you need this over using [twine](https://twine.readthedocs.io/) directly

## Installation

If you installed `pdm` via `pipx`:

```sh
pipx inject pdm pdm-publish
```

or `brew`:

```sh
$(brew --prefix pdm)/libexec/bin/python -m pip install pdm-publish
```

or `pip`:

```sh
pip install --user pdm-publish
```

## Usage

`pdm-publish` enables `pdm` to publish packages to PyPI by wrapping [twine](https://twine.readthedocs.io/en/latest/) internally.
For example, to build and publish:

```sh
# Using token auth
pdm publish --password token
# To test PyPI using basic auth
pdm publish -r testpypi -u username -P password
# To custom index
pdm publish -r https://custom.index.com/
```

Full usage:

```sh
$ pdm publish --help
Upload artifacts to a remote repository

Usage:

Options:
  -h, --help            show this help message and exit
  -v, --verbose         -v for detailed output and -vv for more detailed
  -g, --global          Use the global project, supply the project root with
                        `-p` option
  -p PROJECT_PATH, --project PROJECT_PATH
                        Specify another path as the project root, which
                        changes the base of pyproject.toml and __pypackages__
  -r REPOSITORY, --repository REPOSITORY
                        The repository name or url to publish the package to
                        [env var: PDM_PUBLISH_REPO]
  -u USERNAME, --username USERNAME
                        The username to access the repository [env var:
                        PDM_PUBLISH_USERNAME]
  -P PASSWORD, --password PASSWORD
                        The password to access the repository [env var:
                        PDM_PUBLISH_PASSWORD]
  --dry-run             Perform all actions except upload the package
  --no-build            Don't build the package before publishing
```

## Configuration

| Config Item        | Description                           | Default Value | Available in Project | Env var                |
| ------------------ | ------------------------------------- | ------------- | -------------------- | ---------------------- |
| `publish.repo`     | PyPI repo name (pypi/testpypi) or url | `pypi`        | True                 | `PDM_PUBLISH_REPO`     |
| `publish.username` | PyPI username                         | `__token__`   | True                 | `PDM_PUBLISH_USERNAME` |
| `publish.password` | PyPI password                         |               | True                 | `PDM_PUBLISH_PASSWORD` |

## Links

- [Changelog](https://github.com/branchvincent/pdm-publish/releases)
- [Contributing](CONTRIBUTING.md)
