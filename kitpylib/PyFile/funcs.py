import os, time

def exists(filename: str, msg=True):
    '''Confirm a file exists or not(Any files are okay).'''
    a = os.path.isfile(filename)
    if not msg: 
        return a
    else:
        if a:
            print(f'UserWarning: File `{filename}` already exists!')
        else:
            print(f'UserWarning: File `{filename}` does not exist!')

def make(filename: str, blank=True):
    '''If `blank`, the system will leave the txt file blank.
       If not, the system will add author and time to the file.'''
    with open(filename, 'w', encoding='utf-8') as f:
        if blank: 
            pass
        else:
            f.write(f'Author: {os.getcwd()}\nTime: ')
            f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    print(f'The file `{filename}` is created successfully.')

def makefile(filename: str, restart=False, blank=True):
    if exists(filename, msg=False):
        exists(filename)
        if restart:
            print('Ignore warning. Restart file.')
            make(filename, blank)
    else: 
        make(filename, blank)
        
def rename(oldname: str, newname: str):
    os.rename(oldname, newname)
    print(f'The file `{oldname}` has changed to file `{newname}`.')

def delfile(filename: str):
    os.remove(filename)
    print(f'The file `{filename}` is deleted successfully.')
