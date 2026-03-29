import numpy as np
from .funcs import exists

class File:
    '''A class to process files.'''
    def __init__(self, filename: str):
        if exists(filename, msg=False):
            self.filename = filename
        else:
            exists(filename) 
    
    def read_data(self, skiprows=2):
        return np.loadtxt(self.filename, skiprows=skiprows)
    
    def write(self, string: str):
        with open(self.filename, 'a') as f:
            f.write(string+'\n')
        print(f'The file `{self.filename}` is saved successfully.')
        
    def load_all(self):
        with open(self.filename, 'r') as f:
            for i in f:
                print(i, end='')
        
    def read_text(self, skiprows=2): 
        with open(self.filename, 'r') as f:
            for i in range(skiprows):
                f.readline()
            return [j for j in f]
        
    def setText(self, a: list):
        with open(self.filename, 'w') as f:
            if isinstance(a, list):
                for i in a:
                    f.write(i+'\n')