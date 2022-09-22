# Python Cpp bindings

Explorations in how to use Python, C++, and bindings between the two systems. Build compiled code in multiple environments via GitHub Actions. Key technologies used include [pybind11](https://pybind11.readthedocs.io/en/stable/) and [cibuildwheel](https://cibuildwheel.readthedocs.io/en/stable/).

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


TODO
- add tests in cibuildwheel commands
