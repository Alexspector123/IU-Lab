import numpy as np
from math import log
from scipy.integrate import quad

def f(x):
    return np.log(x)

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    total = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        total += f(a + i * h)
    return total * h

a = 1
b = 2

T1 = trapezoidal_rule(f, a, b, n=1)
T4 = trapezoidal_rule(f, a, b, n=4)

exact_value, _ = quad(f, a, b)

def relative_error(approx, exact):
    return abs((approx - exact) / exact) * 100 

print("Trapezoidal Rule with n=1:", T1)
print("Trapezoidal Rule with n=4:", T4)
print("Exact Value:", exact_value)
print("Relative Error (n=1):", relative_error(T1, exact_value), "%")
print("Relative Error (n=4):", relative_error(T4, exact_value), "%")
