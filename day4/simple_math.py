"""
A collection of simple math operations
"""

def simple_add(a,b):
    """
    add(a, b)

    The sum of two numbers.
    """
    return a+b

def simple_sub(a,b):
    """
    simple_sub(a, b)
    
    The subtraction of two numbers.
    """
    return a-b

def simple_mult(a,b):
    """
    simple_mult(a, b)
    
    The multiplication of two numbers.
    """
    return a*b

def simple_div(a,b):
    """
    simple_div(a, b)
    
    The division of two numbers.
    """
    return a/b

def poly_first(x, a0, a1):
    """
    poly_first(a, b)
    
    A first order of polynomial constracted with a0, a1.
    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """
    poly_second(a, b)
    
    A second order of polynomial constracted with a0, a1.
    """
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
