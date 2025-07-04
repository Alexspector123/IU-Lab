import math
import numpy as np
import matplotlib.pyplot as plt

# Data points
x_values = [0, math.pi / 2, math.pi]
y_values = [math.sin(x) for x in x_values]
x_target = math.pi / 4
true_value = math.sin(x_target)

# 1. Linear interpolation (piecewise)
def linear_interpolation(x_vals, y_vals, x):
    for i in range(len(x_vals) - 1):
        if x_vals[i] <= x <= x_vals[i + 1]:
            xi, xi1 = x_vals[i], x_vals[i + 1]
            yi, yi1 = y_vals[i], y_vals[i + 1]
            return yi + ((yi1 - yi) / (xi1 - xi)) * (x - xi)
    raise ValueError("x out of bounds")

# 2. Lagrange interpolation
def lagrange_interpolation(x_vals, y_vals, x):
    total = 0
    n = len(x_vals)
    for j in range(n):
        term = y_vals[j]
        for i in range(n):
            if i != j:
                term *= (x - x_vals[i]) / (x_vals[j] - x_vals[i])
        total += term
    return total

# 3. Newton interpolation
def newton_divided_diff(x, y):
    n = len(x)
    table = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        table[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x[i + j] - x[i])
    coeffs = [table[0][j] for j in range(n)]
    return coeffs

def newton_polynomial(x_data, coeffs, x):
    result = coeffs[0]
    product = 1
    for i in range(1, len(coeffs)):
        product *= (x - x_data[i - 1])
        result += coeffs[i] * product
    return result

# Apply all three methods
linear_result = linear_interpolation(x_values, y_values, x_target)
lagrange_result = lagrange_interpolation(x_values, y_values, x_target)
newton_coeffs = newton_divided_diff(x_values, y_values)
newton_result = newton_polynomial(x_values, y_values, x_target)

# Compute errors
linear_error = abs(true_value - linear_result)
lagrange_error = abs(true_value - lagrange_result)
newton_error = abs(true_value - newton_result)

# Output results
print(f"True value: sin(π/4) = {true_value}")
print("\nInterpolation Results and Errors at x = π/4:")

print(f"Linear interpolation:   {linear_result:.6f} | Absolute Error: {linear_error:.6f}")
print(f"Lagrange interpolation: {lagrange_result:.6f} | Absolute Error: {lagrange_error:.6f}")
print(f"Newton:   {newton_result:.6f} | Absolute Error: {newton_error:.6f}")

# Function and domain
x_dense = np.linspace(0, math.pi, 200)
true_y = np.sin(x_dense)

# Interpolations over the dense x values
linear_y = [linear_interpolation(x_values, y_values, xi) for xi in x_dense]
lagrange_y = [lagrange_interpolation(x_values, y_values, xi) for xi in x_dense]
newton_y = [newton_polynomial(x_values, newton_coeffs, xi) for xi in x_dense]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x_dense, true_y, label='sin(x)', color='black', linewidth=2)
plt.plot(x_dense, linear_y, '--', label='Linear Interpolation', color='blue')
plt.plot(x_dense, lagrange_y, ':', label='Lagrange Interpolation', color='green')
plt.plot(x_dense, newton_y, '-.', label='Newton Interpolation', color='red')

# Plot original data points
plt.scatter(x_values, y_values, color='black', zorder=5, label='Data Points')

# Mark π/4
plt.axvline(x=math.pi/4, color='gray', linestyle='--', alpha=0.6)
plt.text(math.pi/4 + 0.05, 0.1, 'π/4', fontsize=12)

plt.title('Interpolation Methods vs sin(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()