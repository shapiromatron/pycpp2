from importlib.metadata import version
from .doubles import double_add
from . import bleep

__version__ = version("pybmds")
__all__ = ["__version__", "bleep", "double_add"]
