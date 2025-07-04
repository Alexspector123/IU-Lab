import numpy as np

def jacobi_method(A, b, tol=1e-6, max_iter=100):
    n = len(A)
    x = np.zeros(n)
    x_new = np.zeros(n)
    iter_count = 0

    for _ in range(max_iter):
        for i in range(n):
            x_new[i] = (b[i] - np.sum(A[i, :i] * x[:i]) - np.sum(A[i, i+1:] * x[i+1:])) / A[i, i]
        
        error = np.linalg.norm(x_new - x, ord=np.inf)
        if error < tol:
            return x_new, iter_count
        x = x_new.copy()
        iter_count += 1
    
    return x_new, iter_count  # Return max_iter if not converged

def gauss_seidel_method(A, b, tol=1e-6, max_iter=100):
    n = len(A)
    x = np.zeros(n)
    iter_count = 0

    for _ in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            x[i] = (b[i] - np.sum(A[i, :i] * x[:i]) - np.sum(A[i, i+1:] * x[i+1:])) / A[i, i]
        
        error = np.linalg.norm(x - x_old, ord=np.inf)
        if error < tol:
            return x, iter_count
        iter_count += 1
    
    return x, iter_count  # Return max_iter if not converged

def solve_iterative_methods():
    A = np.array([[5, -2, 3], [2, 5, -1], [1, 3, 5]], dtype=float)
    b = np.array([10, 4, 8], dtype=float)
    
    jacobi_solution, jacobi_iters = jacobi_method(A, b)
    gauss_seidel_solution, gauss_seidel_iters = gauss_seidel_method(A, b)

    print(f"Jacobi Method achieved in {jacobi_iters} iterations.")
    print(f"Solution: x = {jacobi_solution[0]:.6f}, y = {jacobi_solution[1]:.6f}, z = {jacobi_solution[2]:.6f}\n")

    print(f"Gauss-Seidel Method achieved in {gauss_seidel_iters} iterations.")
    print(f"Solution: x = {gauss_seidel_solution[0]:.6f}, y = {gauss_seidel_solution[1]:.6f}, z = {gauss_seidel_solution[2]:.6f}")

if __name__ == "__main__":
    solve_iterative_methods()
