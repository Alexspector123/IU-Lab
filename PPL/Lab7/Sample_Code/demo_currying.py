"""
We can use higher-order functions to convert a function 
that takes multiple arguments into a chain of functions 
that each take a single argument. 

More specifically, given a function f(x, y), 
we can define a function g such that g(x)(y) is equivalent to f(x, y). 
Here, g is a higher-order function that takes in a single argument x 
and returns another function that takes in a single argument y. 

This transformation is called currying.
"""


# traditional way:
def f(x, y):
    return x * y
# function call: f(x, y)
def f(x):
    def g(y):
        return x* y
    return g

print(f(5)(3))

def f2(x):
    def g(y):
        def h(z):
            return x * y + z
        return h
    return g

print(f2(5)(3)(4))
