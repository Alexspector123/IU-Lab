import numpy as np
import matplotlib.pyplot as plt
from math import exp
from scipy.integrate import quad

def f(x):
    return np.exp(-x**2)

# Trapezoidal Rule
def trapezoidal(f, a, b, n):
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n):
        result += 2 * f(a + i * h)
    return (h / 2) * result

# Simpson's 1/3 Rule
def simpson_13(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be even for Simpson's 1/3 Rule")
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n):
        result += 4 * f(a + i * h) if i % 2 != 0 else 2 * f(a + i * h)
    return (h / 3) * result

# Simpson's 3/8 Rule
def simpson_38(f, a, b, n):
    if n % 3 != 0:
        raise ValueError("n must be a multiple of 3 for Simpson's 3/8 Rule")
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n):
        if i % 3 == 0:
            result += 2 * f(a + i * h)
        else:
            result += 3 * f(a + i * h)
    return (3 * h / 8) * result

a, b = 0, 1
n = 6
exact_value, _ = quad(f, a, b)

trap_val = trapezoidal(f, a, b, n)
simp13_val = simpson_13(f, a, b, n)
simp38_val = simpson_38(f, a, b, n)

errors = {
    "Trapezoidal": abs(trap_val - exact_value),
    "Simpson 1/3": abs(simp13_val - exact_value),
    "Simpson 3/8": abs(simp38_val - exact_value)
}

print("{:<15} {:<20} {:<20}".format("Method", "Approximation", "Absolute Error"))
print("-" * 55)
print("{:<15} {:<20.10f} {:<20.10f}".format("Trapezoidal", trap_val, errors["Trapezoidal"]))
print("{:<15} {:<20.10f} {:<20.10f}".format("Simpson 1/3", simp13_val, errors["Simpson 1/3"]))
print("{:<15} {:<20.10f} {:<20.10f}".format("Simpson 3/8", simp38_val, errors["Simpson 3/8"]))

plt.figure(figsize=(8, 5))
plt.bar(errors.keys(), errors.values(), color=['skyblue', 'lightgreen', 'salmon'])
plt.title('Absolute Error Comparison of Numerical Integration Methods')
plt.ylabel('Absolute Error')
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
