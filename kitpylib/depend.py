import kitpylib.PyFile as pf
import kitpylib as kpl

def create_files(module, year, author):
    pf.makefile('README.rst', restart=True)
    a = pf.File('README.rst')
    a.write(module.__doc__)
    pf.makefile('LICENSE.txt', restart=True)
    a = pf.File('LICENSE.txt')
    copr = f'MIT LICENSE\n\nCopyright (c) {year}, {author}'
    a.write(copr + kpl.mit_license)
    
def smy_setup(pkg, **attrs):
    '''S_My setup tools.'''
    kpl.pkg_setup(pkg, 
              classifiers = ['Operating System :: Microsoft :: Windows :: Windows 11',
                             'Operating System :: Microsoft :: Windows :: Windows 7',
                             'Programming Language :: Python :: 3',
                             'Programming Language :: Python :: 3.9',
                             'License :: OSI Approved :: MIT License'],
              long_description = pkg.__doc__,
              long_description_content_type='text/x-rst',
              **attrs)