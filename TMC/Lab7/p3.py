# Given data
x_vals = [1.0, 1.1, 1.2, 1.3, 1.4]
f_vals = [2.71, 3.00, 3.32, 3.67, 4.05]
h = 0.1

# Central difference function for discrete data
def central_difference(x_data, f_data, h, target_x):
    try:
        i = x_data.index(target_x)
        if i == 0 or i == len(x_data) - 1:
            raise ValueError("Cannot compute central difference at the boundary point.")
        return (f_data[i + 1] - f_data[i - 1]) / (2 * h)
    except ValueError as e:
        return str(e)

# Points to evaluate
target_points = [1.1, 1.2, 1.3]

# Compute and display results
print("Central Difference Approximation:")
for x in target_points:
    result = central_difference(x_vals, f_vals, h, x)
    print(f"f'({x}) ≈ {result:.4f}" if isinstance(result, float) else f"Error at x = {x}: {result}")
