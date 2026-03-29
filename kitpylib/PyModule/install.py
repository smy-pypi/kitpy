from setuptools import setup, find_packages

def confirm_info(all_modules):
    '''Confirm name, version of a module.'''
    name = all_modules.__name__
    version = all_modules.__version__
    return name, version

def mod_setup(module, **attrs):
    '''
    modules' setup. Need version string(__version__).
    
    **attrs**: except `name`, `version` and `py_modules`.
    '''
    _name, _version = confirm_info(module)
    setup(name=_name, version=_version, py_modules=[_name], **attrs)
    
def pkg_setup(package, **attrs):
    '''
    packages' setup. Need version string(__version__).
    
    **attrs**: except `name`, `version` and `packages`.
    '''
    _name, _version= confirm_info(package)
    setup(name=_name, packages=find_packages(), version=_version, **attrs)
