def f(x):
    return x**3 - x - 2

def bisection_method(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Bisection method fails. f(a) and f(b) must have opposite signs.")
        return None
    
    iter_count = 0
    c_old = a
    
    print(f"{'Iter':<5}{'a':<10}{'b':<10}{'c':<10}{'f(c)':<15}{'Error (%)':<15}")
    print("-" * 60)
    
    while (b - a) / 2 > tol and iter_count < max_iter:
        c_new = (a + b) / 2
        error = abs((c_new - c_old) / c_new) * 100 if iter_count > 0 else None
        
        print(f"{iter_count:<5}{a:<10.6f}{b:<10.6f}{c_new:<10.6f}{f(c_new):<15.6f}{error if error is not None else 'N/A':<15}")
        
        if f(c_new) == 0:
            return c_new
        elif f(a) * f(c_new) < 0:
            b = c_new
        else:
            a = c_new
        
        c_old = c_new
        iter_count += 1
    
    return (a + b) / 2

root = bisection_method(1, 2)
print("\nApproximate root:", root)