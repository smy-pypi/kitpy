'''
PyFile: A useful module to process files
========================================

How to use
----------

    >>> import kitpylib.PyFile as pf

Available functions and class
-----------------------------
This module provides functions and a class to process txt files::
    
    exists(function): tell the user whether the txt file exists
    makefile(function): generate a txt file
    delfile(function): delete a txt file
    rename(function): rename a txt file
    File(class): `read` and `write`
       
See documentation for the functions and classes.'''
from . import classes, funcs
from .classes import File
from .funcs import exists, makefile, delfile, rename

del classes, funcs