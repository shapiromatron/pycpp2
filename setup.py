from glob import glob
from setuptools import setup, find_packages

from pybind11.setup_helpers import ParallelCompile
from pybind11.setup_helpers import Pybind11Extension, build_ext


__version__ = "0.0.1"

ParallelCompile("NPY_NUM_BUILD_JOBS").install()

setup(
    name="bloop",
    version=__version__,
    python_requires=">=3.9",
    cmdclass={"build_ext": build_ext},
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    ext_modules=[
        Pybind11Extension(
            "bloop.bleep",
            sorted(glob("cpp/*.cpp")),  # Sort for reproducibility
            define_macros = [('VERSION_INFO', __version__)],
        )
    ]
)
