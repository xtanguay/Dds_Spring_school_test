"""bw_tests."""

# https://docs.python.org/3/tutorial/modules.html#importing-from-a-package
__all__ = (
    "__version__",
    "hello_word",
)



__version__ = "0.0.1"

from .printing import hello_world