import numpy as np
import matplotlib.pyplot as plt

x = 2.0
h_values = [0.1, 0.01, 0.001]
exact = 1 / x  # Exact derivative: 1/x
rel_errors = []

print("Error Behavior for ln(x) at x = 2 (Central Difference)")
for h in h_values:
    f_x_plus_h = np.log(x + h)
    f_x_minus_h = np.log(x - h)
    cd = (f_x_plus_h - f_x_minus_h) / (2 * h)
    abs_error = abs(exact - cd)
    rel_error = (abs_error / exact) * 100
    rel_errors.append(rel_error)
    print(f"h = {h}: Derivative = {cd:.9f}, Absolute Error = {abs_error:.9f}, Relative Error = {rel_error:.6f}%")

# Plotting
plt.figure(figsize=(8, 6))
plt.loglog(h_values, rel_errors, 'bo-', label='Relative Error')
plt.xlabel('Step Size (h)')
plt.ylabel('Relative Error (%)')
plt.title('Relative Error vs. Step Size for ln(x) at x = 2')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.savefig('error_vs_h.png')  # Save the plot
plt.show()  # Display the plot