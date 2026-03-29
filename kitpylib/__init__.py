'''
KitPyLib
========

A Python Toolkit Library for developing packages.

How to use
----------
We recommend you to import `kitpylib` as ``kpl``:\n
  >>> import kitpylib as kpl
  >>> kpl.fplot2d(lambda x: x**3, 0, 2)
  
Use the built-in ``help`` function to view a function's docstring:\n
  >>> help(kpl.fplot2d)
  ... # doctest: +SKIP
  
Available subpackages
---------------------
PyFile
    KitPyLib's subpackage to solve txt file problems
PyWidget
    Not Available(KitPyLib's subpackage about qt widgets)
   
Utilities
---------
__version__
    KitPyLib version string
__copr__
    KitPyLib copyright string
__lic__
    KitPyLib license string
smyinfo
    KitPyLib Developer Information
'''
from . import PyFile, PyMath, PyModule, PyPlot, init, depend
from .PyMath import *
from .PyModule import *
from .PyPlot import *
from .init import *
from .init import __copr__, __lic__, __version__
from .depend import *
del PyMath, PyModule, PyPlot, init, depend