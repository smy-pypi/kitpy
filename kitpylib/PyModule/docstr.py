'''A module to generate docstrings for modules.'''

def generate_doc(module: str, abbr: str, func: str):
    '''A function to generate docstring.'''
    string = """
{0}
============================\n    
How to use the documentation
----------------------------
We recommend exploring the docstrings using
`IPython <https://ipython.org>`_, an advanced Python shell with
TAB-completion and introspection capabilities.  See below for further
instructions.\n
The docstring examples assume that `{0}` has been imported as `{1}`::\n
  >>> import {0} as {1}

Use the built-in ``help`` function to view a function's docstring::\n
  >>> help({1}.{2})
  ... # doctest: +SKIP

Utilities
---------
__version__
    {0} version string

Viewing documentation using IPython
----------------------------------- 
To see which functions are available in `{0}`, type ``{1}.<TAB>``
(where ``<TAB>`` refers to the TAB key), or use ``{1}.*{2}*?<ENTER>``
(where ``<ENTER>`` refers to the ENTER key) to narrow down the list.
To view the docstring for a function, use ``{1}.{2}?<ENTER>`` (to view
the docstring) and ``{1}.{2}??<ENTER>`` (to view the source 
code).""".format(module, abbr, func)
    return string