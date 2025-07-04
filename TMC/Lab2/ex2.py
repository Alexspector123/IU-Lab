def f(x):
    return x**2 - 2

def secant_method(x0, x1, tol=1e-6, max_iter=100):
    iter_count = 0
    
    print(f"{'Iter':<5}{'x0':<15}{'x1':<15}{'x2':<15}{'f(x2)':<15}{'Error (%)':<15}")
    print("-" * 75)
    
    while abs(x1 - x0) > tol and iter_count < max_iter:
        if f(x1) - f(x0) == 0:
            print("Division by zero encountered in secant method.")
            return None
        
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        error = abs((x2 - x1) / x2) * 100 if iter_count > 0 else None
        
        print(f"{iter_count:<5}{x0:<15.6f}{x1:<15.6f}{x2:<15.6f}{f(x2):<15.6f}{error if error is not None else 'N/A':<15}")
        
        x0, x1 = x1, x2
        iter_count += 1
    
    return x1

root = secant_method(1, 2)
print("\nApproximate root:", root)