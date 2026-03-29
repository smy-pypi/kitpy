'''A module for 2d special functions.'''
import numpy as np

def tri2d(x):
    '''The 2d triangle function.'''
    return np.where(abs(x) >= 1, 0, 1-abs(x))

def ramp2d(x):
    '''The 2d ramp function.'''
    return np.where(x > 0, abs(x), 0)
    
def rect2d(x):
    '''The 2d rectangle function.'''
    return np.where(abs(x) > 0.5, 0,
                    np.where(abs(x) == 0.5, 0.5, 1))

def sign2d(x):
    '''The 2d sign function.'''
    return np.where(x < 0, -1,
                    np.where(x == 0, 0, 1))

def step2d(x):
    '''The 2d step function.'''
    return np.where(x < 0, 0,
                    np.where(x == 0, 0.5, 1))
   
def gaus2d(x):
    '''The 2d Gaussian Function.'''
    return np.exp(-np.pi*x**2)

def sinc2d(x):
    '''The 2d sinc function.'''
    return np.where(x == 0, 1, np.sin(x)/x)