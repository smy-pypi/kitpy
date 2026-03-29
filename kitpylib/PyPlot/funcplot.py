import numpy as np
from .backend import plot2d
import matplotlib.pyplot as plt

def fplot2d(f, start, stop, num=100, *args, **kwargs):
    '''
    A function to plot 2d functions.
    
    Parameters
    ----------
    f : f(x)
        The function to plot.
    start : number
        The starting value of the sequence.
    stop : number
        The end value of the sequence.
    num : number, optional
        Number of samples to generate. The default is 100.
    *args* : optional
        See documentation of `kpl.plot2d`.
    '''
    a = np.linspace(start, stop, num)
    plot2d(a, f(a), *args, **kwargs)

def fplot3d(f, xstart, xstop, ystart, ystop, num=100):
    '''
    A function to plot 3d functions.

    Parameters
    ==========
    f : f(x)
        The function to plot.
    num : number, optional
        Number of samples to generate. The default is 100.
    
    For X:
    ------
    xstart : int
        The starting value of the sequence x.
    xstop :  int
        The end value of the sequence x.
    
    For Y:
    ------
    ystart : int
        The starting value of the sequence y.
    ystop :  int
        The end value of the sequence y.
    '''
    A = np.linspace(xstart, xstop, num)
    B = np.linspace(ystart, ystop, num)
    a, b = np.meshgrid(A, B)
    c = f(a, b)
    fig, ax = plt.subplots(1, 2, figsize=(9.2, 4), 
                     subplot_kw={'projection':'3d'})
    for i in range(2):
        ax[i].set_zlim(-3,2)
        ax[i].set_xlabel(r'$x$')
        ax[i].set_ylabel(r'$y$')
        ax[i].set_zlabel(r'$f(x,y)$')
        ax[i].view_init(40, -30)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.96, 
                        top=0.96, wspace=0.05)
    p0 = ax[0].plot_wireframe(a,b,c,rcount=40,ccount=40,color='C1')
    p1 = ax[1].plot_surface(a,b,c,rcount=50,ccount=50,color='C1')
    plt.subplots_adjust(left=0.0)