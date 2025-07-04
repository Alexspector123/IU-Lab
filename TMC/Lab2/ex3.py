import math

def f(x):
    return math.cos(x) - x

def df(x):
    return -math.sin(x) - 1

def newton_raphson(x0, tol=1e-6, max_iter=100):
    iter_count = 0
    
    print(f"{'Iter':<5}{'x_old':<15}{'x_new':<15}{'f(x_new)':<15}{'Error (%)':<15}")
    print("-" * 75)
    
    while abs(f(x0)) > tol and iter_count < max_iter:
        if df(x0) == 0:
            print("Derivative is zero. Newton-Raphson method fails.")
            return None
        
        x_new = x0 - f(x0) / df(x0)
        error = abs((x_new - x0) / x_new) * 100 if iter_count > 0 else None
        
        print(f"{iter_count:<5}{x0:<15.6f}{x_new:<15.6f}{f(x_new):<15.6f}{error if error is not None else 'N/A':<15}")
        
        x0 = x_new
        iter_count += 1
    
    return x0

root = newton_raphson(0.5)
print("\nApproximate root:", root)