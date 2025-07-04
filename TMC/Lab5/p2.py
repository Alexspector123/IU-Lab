import numpy as np
import matplotlib.pyplot as plt

# Data points
x_data = np.array([0.1, 0.2, 0.4, 0.6, 0.9, 1.3, 1.5, 1.7, 1.8])
y_data = np.array([0.75, 1.25, 1.45, 1.25, 0.85, 0.55, 0.35, 0.28, 0.18])

# Model function
def model(x, alpha, beta):
    return alpha * x * (1 - np.exp(beta * x))

def compute_jacobian(x, alpha, beta):
    df_dalpha = x * (1 - np.exp(beta * x))
    df_dbeta = alpha * x**2 * np.exp(beta * x)
    return np.vstack((df_dalpha, df_dbeta)).T

# Residual vector D
def compute_residuals(x, y, alpha, beta):
    return y - model(x, alpha, beta)

# Jacobi method for solving Ax = b
def jacobi(A, b, tol=1e-6, max_iter=100):
    n = len(b)
    x = np.zeros_like(b)
    for it in range(max_iter):
        x_new = np.zeros_like(x)
        for i in range(n):
            s = sum(A[i, j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i, i]
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new
        x = x_new
    return x

# Nonlinear regression using Gauss-Newton style iterations
def nonlinear_fit(x, y, alpha_init, beta_init, iterations=10):
    alpha, beta = alpha_init, beta_init

    for i in range(iterations):
        D = compute_residuals(x, y, alpha, beta)
        Z = compute_jacobian(x, alpha, beta)
        ZT_Z = Z.T @ Z
        ZT_D = Z.T @ D

        delta = jacobi(ZT_Z, ZT_D)

        alpha += delta[0]
        beta += delta[1]

    return alpha, beta

# Initial guesses
alpha0 = 1.0
beta0 = -1.0

# Run the fitting
alpha_est, beta_est = nonlinear_fit(x_data, y_data, alpha0, beta0)
print(f"\nEstimated parameters:\n  α4 = {alpha_est:.5f}\n  β4 = {beta_est:.5f}")

# Plot the results
x_plot = np.linspace(min(x_data), max(x_data), 100)
y_plot = model(x_plot, alpha_est, beta_est)

plt.scatter(x_data, y_data, color='red', label='Data points')
plt.plot(x_plot, y_plot, color='blue', label=f'Fitted curve: y = {alpha_est:.3f}x(1 - exp({beta_est:.3f}x))')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Nonlinear Regression Fit')
plt.legend()
plt.show()
