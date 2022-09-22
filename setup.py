from glob import glob
from setuptools import setup

from pybind11.setup_helpers import ParallelCompile
from pybind11.setup_helpers import Pybind11Extension, build_ext


ParallelCompile("NPY_NUM_BUILD_JOBS").install()

setup(
    name='bloop',
    version='0.0.1',
    python_requires=">=3.9",
    cmdclass={"build_ext": build_ext},
    ext_modules=[
        Pybind11Extension(
            "bloop",
            sorted(glob("src/*.cpp")),  # Sort for reproducibility
        )
    ]
)
