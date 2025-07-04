import numpy as np

def jacobi_method(A, b, tol=1e-6, max_iter=100):
    n = len(A)
    x = np.zeros(n)
    x_new = np.zeros(n)
    iter_count = 0
    
    print(f"{'Iter':<5}{'x':<15}{'y':<15}{'z':<15}")
    print("-" * 60)
    
    for _ in range(max_iter):
        for i in range(n):
            x_new[i] = (b[i] - np.sum(A[i, :i] * x[:i]) - np.sum(A[i, i+1:] * x[i+1:])) / A[i, i]
        
        error = np.linalg.norm(x_new - x, ord=np.inf)
        if iter_count < 3:
            print(f"{iter_count:<5}{x_new[0]:<15.6f}{x_new[1]:<15.6f}{x_new[2]:<15.6f}")
        
        if error < tol:
            return x_new
        x = x_new.copy()
        iter_count += 1
    
    return x_new

def gauss_seidel_method(A, b, tol=1e-6, max_iter=100):
    n = len(A)
    x = np.zeros(n)
    iter_count = 0
    
    print(f"{'Iter':<5}{'x':<15}{'y':<15}{'z':<15}")
    print("-" * 60)
    
    for _ in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            x[i] = (b[i] - np.sum(A[i, :i] * x[:i]) - np.sum(A[i, i+1:] * x[i+1:])) / A[i, i]
        
        error = np.linalg.norm(x - x_old, ord=np.inf)
        if iter_count < 3:
            print(f"{iter_count:<5}{x[0]:<15.6f}{x[1]:<15.6f}{x[2]:<15.6f}")
        
        if error < tol:
            return x
        iter_count += 1
    
    return x

def solve_iterative_methods():
    A = np.array([[5, -2, 3], [2, 5, -1], [1, 3, 5]], dtype=float)
    b = np.array([10, 4, 8], dtype=float)
    
    print("\nSolving using Jacobi Method:")
    jacobi_solution = jacobi_method(A, b)
    print(f"\nJacobi Solution in 100th approximation:\n x = {jacobi_solution[0]}\n y = {jacobi_solution[1]}\n z = {jacobi_solution[2]}")
    
    print("\nSolving using Gauss-Seidel Method:")
    gauss_seidel_solution = gauss_seidel_method(A, b)
    print(f"\nGauss-Seidel Solution in 100th approximation:\n x = {gauss_seidel_solution[0]}\n y = {gauss_seidel_solution[1]}\n z = {gauss_seidel_solution[2]}")

if __name__ == "__main__":
    solve_iterative_methods()