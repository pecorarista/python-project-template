# python-project-template
[![CircleCI](https://circleci.com/gh/pecorarista/python-project-template.svg?style=svg)](https://circleci.com/gh/pecorarista/python-project-template)

A template for Python projects. This sample package is assumed to be released as a CLI tool.

## Environment
Install dependencies by `pipenv`.

```bash
pipenv install  # Add `--dev` for development 
pipenv shell
```

## How to Use
```bash
cp example.toml config.toml
pipenv run python -m mypkg -d resources/corpora
```

## Coding Style

Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/).

```bash
flake8 mypkg tests
```

## Order of import-statements

Order import-statements as the following.

```python
import python_standard_library

import third_party_library

from mypkg.some_module import some_function
from mypkg.another_module import another_function
```

This is automatically achieved by `isort`.

```bash
isort --recursive mypkg tests
```

## Testing

Test the source code before merging your changes into the master branch.

```bash
pytest
```

The settings are written in Section `[tool:pytest]` in [setup.cfg](setup.cfg) and [tests/conftest.py](tests/conftest.py).
