# A distributable python/cpp package

Explorations in how to use Python, C++, and bindings between the two systems. Build compiled code in multiple environments via GitHub Actions. Key technologies used include [pybind11](https://pybind11.readthedocs.io/en/stable/) and [cibuildwheel](https://cibuildwheel.readthedocs.io/en/stable/).

The project does the following:

- Builds a simple cpp package
- Builds a python interface to the cpp package
- Has some tests to ensure the cpp package works correctly from python
- Automatically builds the python package on Mac, Linux, and Windows

## Quickstart

```bash
# setup environment
python -m venv venv
source venv/bin/activate
pip install -U pip wheel
pip install -r requirements.txt

# compile code and install package locally
pip install -e .

# run tests to make sure it works and imports into python
py.test

# build package locally
python -m build
```
