import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return (x - 2)**2 + np.sin(5 * x)

# Golden Section Search implementation
def golden_section_search(f, a, b, tol=1e-5):
    gr = (np.sqrt(5) + 1) / 2  # Golden ratio

    c = b - (b - a) / gr
    d = a + (b - a) / gr

    while abs(b - a) > tol:
        if f(c) < f(d):
            b = d
        else:
            a = c

        # Recalculate points
        c = b - (b - a) / gr
        d = a + (b - a) / gr

    x_min = (b + a) / 2
    return x_min, f(x_min)

# Run the search
x_min, y_min = golden_section_search(f, 0, 4)

# Print the results
print(f"Minimum value found at x = {x_min:.5f}")
print(f"Minimum value of f(x) = {y_min:.5f}")

# Plot the function and minimum
x_vals = np.linspace(0, 4, 500)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label="f(x)")
plt.plot(x_min, y_min, 'ro', label=f"Minimum: x={x_min:.5f}")
plt.title("Golden Section Search Result")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
