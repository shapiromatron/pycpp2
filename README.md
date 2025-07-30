# A distributable python/cpp package

Explorations in how to use Python, C++, and bindings between the two systems. Build compiled code in multiple environments via GitHub Actions. Key technologies used include [pybind11](https://pybind11.readthedocs.io/en/stable/) and [cibuildwheel](https://cibuildwheel.readthedocs.io/en/stable/).

The project does the following:

- Builds a simple cpp package
- Builds a python interface to the cpp package
- Has some tests to ensure the cpp package works correctly from python
- Automatically builds the packages on Mac, Linux, and Windows

## Quickstart

```bash
# setup environment
uv venv --python=3.13 --prompt pycpp
source .venv/bin/activate
uv pip install -e ".[dev]"

# run tests to make sure it works and imports into python
py.test

# build package locally
python -m build

# generate stubs for C++ file
stubgen -p bloop.bleep -o src
```
