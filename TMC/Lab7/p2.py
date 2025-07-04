import math

# Define the function
def f(x):
    return math.exp(-x**2)

# Exact second derivative of f''(x) = (4x^2 - 2) * e^(-x^2)
def f_double_prime_exact(x):
    return (4 * x**2 - 2) * math.exp(-x**2)

# Given parameters
x = 0.5
h = 0.1

# Central Difference Approximation for second derivative
f_x_plus = f(x + h)
f_x = f(x)
f_x_minus = f(x - h)

f_double_prime_approx = (f_x_plus - 2 * f_x + f_x_minus) / h**2

f_double_prime_true = f_double_prime_exact(x)

# Error calculations
abs_error = abs(f_double_prime_approx - f_double_prime_true)
rel_error = abs_error / abs(f_double_prime_true) * 100

# Print results
print(f"At x = {x}, with h = {h}")
print(f"\nApproximate f''(x) using Central Difference: {f_double_prime_approx:.6f}")
print(f"Exact f''(x): {f_double_prime_true:.6f}")
print(f"\nAbsolute Error: {abs_error:.6e}")
print(f"Relative Error: {rel_error:.2f}%")
