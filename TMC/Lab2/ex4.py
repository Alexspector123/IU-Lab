import math

def f(x):
    return x**3 - x - 2

def df(x):
    return 3*x**2 - 1

def bisection_method(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Bisection method fails. f(a) and f(b) must have opposite signs.")
        return None, 0
    
    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2
        if f(c) == 0:
            return c, iter_count
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iter_count += 1
    
    return (a + b) / 2, iter_count

def secant_method(x0, x1, tol=1e-6, max_iter=100):
    iter_count = 0
    while abs(x1 - x0) > tol and iter_count < max_iter:
        if f(x1) - f(x0) == 0:
            print("Division by zero encountered in secant method.")
            return None, 0
        
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0, x1 = x1, x2
        iter_count += 1
    
    return x1, iter_count

def newton_raphson(x0, tol=1e-6, max_iter=100):
    iter_count = 0
    while abs(f(x0)) > tol and iter_count < max_iter:
        if df(x0) == 0:
            print("Derivative is zero. Newton-Raphson method fails.")
            return None, 0
        
        x0 = x0 - f(x0) / df(x0)
        iter_count += 1
    
    return x0, iter_count

bisection_root, bisection_iters = bisection_method(1, 2)
secant_root, secant_iters = secant_method(1, 2)
newton_root, newton_iters = newton_raphson(1.5)

print("Method\t\tRoot\t\t\tIterations")
print(f"Bisection\t{bisection_root}\t{bisection_iters}")
print(f"Secant\t\t{secant_root}\t{secant_iters}")
print(f"Newton-Raphson\t{newton_root}\t{newton_iters}")