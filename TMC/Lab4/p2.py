import numpy as np
import matplotlib.pyplot as plt

# Define the function and its derivative
def f(x):
    return x**4 - 3*x**3 + 2

def df(x):
    return 4*x**3 - 9*x**2

# Gradient descent implementation
def gradient_descent(df, x0, alpha, max_iter=100, tol=1e-6):
    x_vals = [x0]
    x = x0
    for _ in range(max_iter):
        try:
            grad = df(x)
            x_new = x - alpha * grad
        except OverflowError:
            print("Overflow detected. Gradient too large.")
            break

        if abs(x_new) > 1e6:  # Arbitrary large value to detect divergence
            print("Divergence detected. x became too large.")
            break

        x_vals.append(x_new)
        if abs(x_new - x) < tol:
            break
        x = x_new
    return x_vals

# Plotting function
def plot_convergence(x_lists, alphas):
    plt.figure(figsize=(10, 6))
    for x_vals, alpha in zip(x_lists, alphas):
        plt.plot(range(len(x_vals)), x_vals, label=f'α = {alpha}')
    
    plt.title('Gradient Descent Convergence (x vs Iterations)')
    plt.xlabel('Iterations')
    plt.ylabel('x value')
    plt.grid(True)
    plt.legend()
    plt.show()

# Main function
def run_experiment():
    x0 = 0.5
    alphas = [0.01, 0.1, 0.3]
    results = []

    for alpha in alphas:
        x_vals = gradient_descent(df, x0, alpha)
        results.append(x_vals)
        print(f"\nα = {alpha} converged to x ≈ {x_vals[-1]:.5f} in {len(x_vals)-1} iterations")

    plot_convergence(results, alphas)

if __name__ == "__main__":
    run_experiment()
