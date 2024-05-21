# bw_tests

[![PyPI](https://img.shields.io/pypi/v/upload_to_pypi_tutorial.svg)][pypi status]
[![Status](https://img.shields.io/pypi/status/upload_to_pypi_tutorial.svg)][pypi status]
[![Python Version](https://img.shields.io/pypi/pyversions/upload_to_pypi_tutorial)][pypi status]
[![License](https://img.shields.io/pypi/l/upload_to_pypi_tutorial)][license]

[![Read the documentation at https://upload_to_pypi_tutorial.readthedocs.io/](https://img.shields.io/readthedocs/upload_to_pypi_tutorial/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/xtanguay/upload_to_pypi_tutorial/actions/workflows/python-test.yml/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/xtanguay/upload_to_pypi_tutorial/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi status]: https://pypi.org/project/upload_to_pypi_tutorial/
[read the docs]: https://upload_to_pypi_tutorial.readthedocs.io/
[tests]: https://github.com/xtanguay/upload_to_pypi_tutorial/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/xtanguay/upload_to_pypi_tutorial
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

## Installation

You can install _bw_tests_ via [pip] from [PyPI]:

```console
$ pip install bw_tests
```

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide][Contributor Guide].

## License

Distributed under the terms of the [MIT license][License],
_bw_tests_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue][Issue Tracker] along with a detailed description.


<!-- github-only -->

[command-line reference]: https://upload_to_pypi_tutorial.readthedocs.io/en/latest/usage.html
[License]: https://github.com/xtanguay/upload_to_pypi_tutorial/blob/main/LICENSE
[Contributor Guide]: https://github.com/xtanguay/upload_to_pypi_tutorial/blob/main/CONTRIBUTING.md
[Issue Tracker]: https://github.com/xtanguay/upload_to_pypi_tutorial/issues


## Building the Documentation

You can build the documentation locally by installing the documentation Conda environment:

```bash
conda env create -f docs/environment.yml
```

activating the environment

```bash
conda activate sphinx_upload_to_pypi_tutorial
```

and [running the build command](https://www.sphinx-doc.org/en/master/man/sphinx-build.html#sphinx-build):

```bash
sphinx-build docs _build/html --builder=singlehtml --jobs=auto --write-all; open _build/html/index.html
```