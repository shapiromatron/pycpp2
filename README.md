# A distributable python/cpp package

Explorations in how to use Python, C++, and bindings between the two systems. Build compiled code in multiple environments via GitHub Actions. Key technologies used include [pybind11](https://pybind11.readthedocs.io/en/stable/) and [cibuildwheel](https://cibuildwheel.readthedocs.io/en/stable/).

The project does the following:

- Builds a simple cpp package
- Builds a python interface to the cpp package
- Has some tests to ensure the cpp package works correctly from python
- Automatically builds the python package on Mac, Linux, and Windows

## Quickstart

```bash

# required for mac?
export "CC=/opt/homebrew/bin/gcc-14"
export "CXX=/opt/homebrew/bin/g++-14"

# setup environment
uv venv --python=3.12 venv
source venv/bin/activate
uv pip install -e ".[dev]"

poe build
poe test
```
