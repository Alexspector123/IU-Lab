import math

# Given function and its exact derivative
def f(x):
    return math.sin(x)

def f_exact_derivative(x):
    return math.cos(x)

# Given parameters
xi = math.pi / 4
h = 0.1
xi_minus_1 = xi - h
xi_plus_1 = xi + h

# Approximate derivatives
forward_diff = (f(xi_plus_1) - f(xi)) / h
backward_diff = (f(xi) - f(xi_minus_1)) / h
central_diff = (f(xi_plus_1) - f(xi_minus_1)) / (2 * h)

# Exact derivative
true_value = f_exact_derivative(xi)

# Error calculations
def compute_errors(approx, true):
    abs_error = abs(approx - true)
    rel_error = abs_error / abs(true) * 100  # relative error in %
    return abs_error, rel_error

fd_abs, fd_rel = compute_errors(forward_diff, true_value)
bd_abs, bd_rel = compute_errors(backward_diff, true_value)
cd_abs, cd_rel = compute_errors(central_diff, true_value)

# Print results
print(f"At x = π/4 ≈ {xi:.5f}, with h = {h}")
print("\nApproximate Derivatives:")
print(f"  Forward Difference: {forward_diff:.6f}")
print(f"  Backward Difference: {backward_diff:.6f}")
print(f"  Central Difference: {central_diff:.6f}")
print(f"\nExact Derivative (cos(π/4)): {true_value:.6f}")

print("\nErrors:")
print(f"  FD - Absolute Error: {fd_abs:.6e}, Relative Error: {fd_rel:.2f}%")
print(f"  BD - Absolute Error: {bd_abs:.6e}, Relative Error: {bd_rel:.2f}%")
print(f"  CD - Absolute Error: {cd_abs:.6e}, Relative Error: {cd_rel:.2f}%")
