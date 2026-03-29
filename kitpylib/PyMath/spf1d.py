import numpy as np

def diff1st(f0, x, h=0.01):
    '''This is the 1st order derivative of a function.\n
    .. math::
        f'(x)=(f(x + h) - f(x - h))/(2*h)'''
    return (f0(x + h) - f0(x - h))/(2*h)

def diff2nd(f0, x, h=0.01):
    '''This is the 2nd order derivative of a function.\n
    .. math::
        f''(x)=(f(x-h)-2*f(x)+f(x+h))/(h*h)'''
    return (f0(x-h)-2*f0(x)+f0(x+h))/(h*h)    

class PC:
    '''PC
    ==
    This is a class of the calculation of pedal curves.\n
    Parameters
    ----------
    f(function), px1, py1(x, y of the point)\n
    Returns
    -------
    a, b: x, y of the function\n
    x, y: x, y of pedal curves\n
    Example
    -------
      >>> f = lambda x: x**2-1
      >>> a = PC(f, 0, 0)
      >>> a.a
      array([-5.       , -4.9989999, -4.9979998, ...,  4.9979998,  4.9989999,
              5.       ])'''
    def __init__(self, f, px1, py1):
        self.a = np.linspace(-5, 5, 10000)
        self.b = f(self.a)
        d = diff1st(f, self.a)
        self.x = (self.a*d**2 + d*(py1 - self.b) + px1)/(d**2 + 1)
        self.y = (py1*d**2 + self.b + px1 - self.a)/(d**2 + 1)