import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.array([3, 4, 5, 7, 8, 9, 11, 12])
y = np.array([1.6, 3.6, 4.4, 3.4, 2.2, 2.8, 3.8, 4.6])

# Cubic equation: ax^3 + bx^2 + cx + d = y
A = np.vstack([x**3, x**2, x, np.ones_like(x)]).T

# Solve the normal equation A^T * A * coeffs = A^T * y to get the coefficients
coeffs = np.linalg.lstsq(A, y, rcond=None)[0]

a, b, c, d = coeffs

y_fit = a * x**3 + b * x**2 + c * x + d

residuals = y - y_fit

ss_total = np.sum((y - np.mean(y))**2)
ss_residual = np.sum(residuals**2)
r_squared = 1 - (ss_residual / ss_total)

sy_x = np.sqrt(ss_residual / (len(x) - 4))

# Coefficients
print("Coefficients: ");
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print(f"d = {d}")

# Output the fitted coefficients and R²
print("Fitted cubic equation: ax^3 + bx^2 + cx + d")
print(f"a = {a:.4f}")
print(f"b = {b:.4f}")
print(f"c = {c:.4f}")
print(f"d = {d:.4f}")
print(f"R² = {r_squared:.4f}")
print(f"Standard Error Sy/x = {sy_x:.4f}")

# Plot the data and the fitted cubic curve
plt.scatter(x, y, color='red', label='Data points')
plt.plot(x, y_fit, color='blue', label=f'Fitted cubic curve: {a:.4f}x³ + {b:.4f}x² + {c:.4f}x + {d:.4f}')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Cubic Fit to Data')
plt.grid(True)
plt.show()
