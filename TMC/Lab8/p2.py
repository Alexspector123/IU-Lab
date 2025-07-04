import numpy as np
from math import sin, pi
from scipy.integrate import quad 

def f(x):
    return np.sin(x)

def simpson_rule(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be even for Simpson's 1/3 Rule")

    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    y = [f(xi) for xi in x]

    result = y[0] + y[-1]
    for i in range(1, n):
        if i % 2 == 0:
            result += 2 * y[i]
        else:
            result += 4 * y[i]

    return result * h / 3

exact_value, _ = quad(f, 0, pi)

S4 = simpson_rule(f, 0, pi, 4)
S6 = simpson_rule(f, 0, pi, 6)

def relative_error(approx, exact):
    return abs((approx - exact) / exact) * 100 

print("Simpson's Rule with n=4:", S4)
print("Simpson's Rule with n=6:", S6)
print("Exact Value:", exact_value)
print("Relative Error (n=4):", relative_error(S4, exact_value), "%")
print("Relative Error (n=6):", relative_error(S6, exact_value), "%")
