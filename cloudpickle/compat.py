import sys
import platform

PYPY = platform.python_implementation() == "PyPy"

if sys.version_info < (3, 8) or PYPY:
    try:
        import pickle5 as pickle  # noqa: F401
        from pickle5 import Pickler  # noqa: F401
    except ImportError:
        import pickle  # noqa: F401
        from pickle import _Pickler as Pickler  # noqa: F401
else:
    import pickle  # noqa: F401
    from _pickle import Pickler  # noqa: F401
