import numpy as np
import matplotlib.pyplot as plt

# Define function and its derivatives
def f(x):
    return np.log(x) + x**2

def df(x):
    return 1/x + 2*x

def d2f(x):
    return -1/(x**2) + 2

# Newton's Method implementation
def newtons_method(df, d2f, x0, tol=1e-6, max_iter=100):
    x_vals = [x0]
    f_vals = [f(x0)]
    x = x0

    for _ in range(max_iter):
        grad = df(x)
        hess = d2f(x)

        if hess == 0:
            print("Zero second derivative. Stopping.")
            break

        x_new = x - grad / hess

        if x_new <= 0:
            print("x out of domain (x <= 0). Stopping.")
            break

        x_vals.append(x_new)
        f_vals.append(f(x_new))

        if abs(x_new - x) < tol:
            break

        x = x_new

    return x_vals, f_vals

# Plotting functions
def plot_convergence(x_vals, f_vals):
    iterations = range(len(x_vals))

    # Plot 1: f(xk) over iterations
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.plot(iterations, f_vals, marker='o', color='blue')
    plt.title("Convergence of f(xₖ)")
    plt.xlabel("Iteration")
    plt.ylabel("f(xₖ)")
    plt.grid(True)

    # Plot 2: xk over iterations
    plt.subplot(1, 2, 2)
    plt.plot(iterations, x_vals, marker='s', color='green')
    plt.title("Values of xₖ")
    plt.xlabel("Iteration")
    plt.ylabel("xₖ")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Run experiment
def run_newton_experiment():
    x0 = 2
    x_vals, f_vals = newtons_method(df, d2f, x0)

    print(f"\nConverged to x ≈ {x_vals[-1]:.6f} with f(x) ≈ {f_vals[-1]:.6f} in {len(x_vals) - 1} iterations")
    plot_convergence(x_vals, f_vals)

if __name__ == "__main__":
    run_newton_experiment()
