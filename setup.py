import re
from glob import glob
from pathlib import Path

from pybind11.setup_helpers import ParallelCompile, Pybind11Extension
from setuptools import setup

ParallelCompile("NPY_NUM_BUILD_JOBS").install()


PY_PACKAGE_NAME = "bloop"


def get_version() -> str:
    fn = Path(__file__).parent / "src" / PY_PACKAGE_NAME / "__init__.py"
    text = Path(fn).read_text()
    version = re.search(r'__version__ = "(.+)"', text)
    if version is None:
        raise ValueError("Version not found")
    return version[1]


setup(
    ext_modules=[
        Pybind11Extension(
            f"{PY_PACKAGE_NAME}.core",
            sorted(glob("cpp/*.cpp")),  # Sort for reproducibility
            define_macros=[("VERSION_INFO", get_version())],
        )
    ]
)
