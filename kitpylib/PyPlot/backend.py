'Matplotlib.PyPlot backend for plotting.'
import matplotlib.pyplot as plt
import matplotlib as mpl

def plot2d(x, y, px=None, py=None, grid=False, title=None, legend=None, 
           axh=False, axv=False, *args):
    '''
    Function plot2d
    
    Example
    -------
    
    With all arguments:
    
       >>> import kitpylib as kpl
       >>> a=[0, 1, 2, 3, 4, 5, 6, 7, 8]
       >>> b=[0, 1, 2, 1, 2, 3, 2, 3, 4]
       >>> kpl.plot2d(a, b, px=a, py=b, grid=True, title='a simple plot', 
                      legend='plot', axh=True, axv=True)
       
    .. image:: image0.png
    
    With only optional arguments:
        
        >>> kp.plot2d(a, b)
        
    .. image:: image1.png
    '''
    if not mpl.get_backend == 'qt5agg':
        plt.switch_backend('qt5agg')
    fig, ax = plt.subplots()
    ax.plot(x, y, label=legend)
    ax.plot(*args)
    if px is not None and py is not None:
        ax.plot(px, py, 'og', ms=7.5, mfc='white', label='point')
    if axh:
        ax.axhline(color='black', linestyle='--', zorder=-1)
    if axv:
        ax.axvline(color='black', linestyle='--', zorder=-1)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(grid)
    if not title == None:
        ax.set_title(title)
    if not legend == None:
        ax.legend(numpoints=1, fontsize='small',
                  loc='upper right', 
                  bbox_to_anchor=(0.9, 0.97))
    fig.show()