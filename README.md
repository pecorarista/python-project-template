# python-project-template

Template for Python projects. The sample package is assumed to be released as a CLI tool.

## Environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Coding Style

Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/).

```bash
flake8 mypkg
flake8 tests
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

```python
isort --recursive mypkg
isort --recursive tests
```

## Testing

Test the source code before merging your changes into the master branch.

```python
pytest
```

The settings are written in Section `[tool:pytest]` in [setup.cfg](setup.cfg) and [tests/conftest.py](tests/conftest.py).
