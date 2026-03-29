'''A module for 3d special functions.'''
from .spf2d import gaus2d, ramp2d, rect2d, sign2d, step2d, tri2d, sinc2d

def tri3d(x, y):
    '''The 3d triangle function.'''
    return tri2d(x)*tri2d(y)

def ramp3d(x, y):
    '''The 3d ramp function.'''
    return ramp2d(x)*ramp2d(y)
  
def rect3d(x, y):
    '''The 3d rectangle function.'''
    return rect2d(x)*rect2d(y)

def sign3d(x, y):
    '''The 3d sign function.'''
    return sign2d(x)*sign2d(y)

def step3d(x, y):
    '''The 3d step function.'''
    return step2d(x)*step2d(y)
  
def gaus3d(x, y):
    '''The 3d Gaussian Function.'''
    return gaus2d(x)*gaus2d(y)

def sinc3d(x, y):
    '''The 3d sinc function.'''
    return sinc2d(x)*sinc2d(y)