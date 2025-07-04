import numpy as np
from math import pi
from scipy.integrate import quad

def f(x):
    return 1 / (1 + x**2)

def simpson_38(f, a, b, n):
    if n % 3 != 0:
        raise ValueError("n must be a multiple of 3 for Simpson's 3/8 Rule")

    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    y = [f(xi) for xi in x]

    result = y[0] + y[-1]

    for i in range(1, n):
        if i % 3 == 0:
            result += 2 * y[i]
        else:
            result += 3 * y[i]

    return (3 * h / 8) * result

a = 0
b = 3
n = 6

S38 = simpson_38(f, a, b, n)

exact_value = np.arctan(b) - np.arctan(a)

def relative_error(approx, exact):
    return abs((approx - exact) / exact) * 100

print("Simpson's 3/8 Rule with n=6:", S38)
print("Exact Value (arctan):", exact_value)
print("Relative Error:", relative_error(S38, exact_value), "%")
