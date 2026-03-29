def bisection(f, a, b, e, showtimes=False):
    '''
    BISECTION
    =========
    A function to find roots of `f(x)=0` by bisection method. 
    `f(a)` and `f(b)` cannot have the same signs.
        
    Parameters
    ----------
    f : func 
        `f` must be continuous. Python function returning a number.
    a : float
        Start of the bracketing interval [a,b].
    b : float
        End of the bracketing interval [a,b].
    e : float
        Accuracy
    showtimes : bool. The default is False.
        Show how many times the calculator use to find the root.
        
    Returns
    -------
    iterations:
        Returns if `showtimes` is True.
    root : float
        Root of `f` between `a` and `b`.
        
    Examples
    --------
    Precise value::\n
      >>> f = lambda x: x**2-1
      >>> root = bisection(f, 0, 2, 0.01)
      >>> root
      1.0
    
    Errors::\n
      >>> root = bisection(f, -2, 2, 0.01)
      ValueError: Incorrect input!
    
    Approximate value::\n
      >>> g = lambda x: -x**3-3*x+5
      >>> root = bisection(g, 1, 2, 0.01)
      >>> root
      1.1484375
      
    `showtimes` is True::\n
      >>> bisection(g, 1, 2, 0.01, showtimes=True)
      Finding root in 7 times.
      1.1484375
      '''
    if f(a)*f(b)<0:
        a1, b1 = a, b
        i = 0
        while not abs(a1-b1) < e:
            i += 1
            c = (a1+b1)/2
            if f(c)==0:
                return c
                break
            if f(c)*f(a1)<0:
                b1 = c
            if f(c)*f(b1)<0:
                a1 = c
        if showtimes:
            print(f'Finding root in {i} times.')
        return a1
    else:
        print('ValueError: Incorrect input!')