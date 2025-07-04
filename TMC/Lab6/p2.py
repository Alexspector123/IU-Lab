# Given data points
x_values = [0, 1, 2, 3]
y_values = [1, 2, 1, 3]

# 1. Lagrange interpolation
def lagrange_interpolation(x_values, y_values, x):
    total = 0
    n = len(x_values)
    for j in range(n):
        term = y_values[j]
        for i in range(n):
            if i != j:
                term *= (x - x_values[i]) / (x_values[j] - x_values[i])
        total += term
    return total

# 2. Estimate f(1.5)
x_to_estimate = 1.5
estimated_value = lagrange_interpolation(x_values, y_values, x_to_estimate)

# Output the result
print(f"Estimated f({x_to_estimate}) using Lagrange interpolation is: {estimated_value}")