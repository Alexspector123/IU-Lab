# Given data points
x_values = [0, 1, 2, 3, 4]
y_values = [1, 2.2, 3.0, 3.6, 4.5]

# 1. Piecewise linear interpolation function
def linear_interpolation(x_values, y_values, x):
    for i in range(len(x_values) - 1):
        xi, xi1 = x_values[i], x_values[i + 1]
        if xi <= x <= xi1:
            yi, yi1 = y_values[i], y_values[i + 1]
            # Apply linear interpolation formula
            return yi + ((yi1 - yi) / (xi1 - xi)) * (x - xi)
    raise ValueError("x is out of bounds of the given data")

# 2. Estimate f(2.5)
x_to_estimate = 2.5
estimated_value = linear_interpolation(x_values, y_values, x_to_estimate)

# Output the result
print(f"Estimated f({x_to_estimate}) using piecewise linear interpolation is: {estimated_value}")
