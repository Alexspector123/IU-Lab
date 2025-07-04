import numpy as np
import time

def gaussian_elimination(A, b):
    start_time = time.time()
    A = A.astype(float)
    b = b.astype(float)
    n = len(A)
    
    for i in range(n):
        max_row = max(range(i, n), key=lambda r: abs(A[r][i]))
        if i != max_row:
            A[[i, max_row]] = A[[max_row, i]]
            b[[i, max_row]] = b[[max_row, i]]
        
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            A[j] -= factor * A[i]
            b[j] -= factor * b[i]
    
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    
    end_time = time.time()
    return x, end_time - start_time, 1

def jacobi_method(A, b, tol=1e-6, max_iter=100):
    start_time = time.time()
    n = len(A)
    x = np.zeros(n)
    x_new = np.zeros(n)
    iter_count = 0
    
    for _ in range(max_iter):
        for i in range(n):
            x_new[i] = (b[i] - np.sum(A[i, :i] * x[:i]) - np.sum(A[i, i+1:] * x[i+1:])) / A[i, i]
        
        error = np.linalg.norm(x_new - x, ord=np.inf)
        if error < tol:
            end_time = time.time()
            return x_new, end_time - start_time, iter_count
        x = x_new.copy()
        iter_count += 1
    
    end_time = time.time()
    return x_new, end_time - start_time, iter_count

def gauss_seidel_method(A, b, tol=1e-6, max_iter=100):
    start_time = time.time()
    n = len(A)
    x = np.zeros(n)
    iter_count = 0
    
    for _ in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            x[i] = (b[i] - np.sum(A[i, :i] * x[:i]) - np.sum(A[i, i+1:] * x[i+1:])) / A[i, i]
        
        error = np.linalg.norm(x - x_old, ord=np.inf)
        if error < tol:
            end_time = time.time()
            return x, end_time - start_time, iter_count
        iter_count += 1
    
    end_time = time.time()
    return x, end_time - start_time, iter_count

def solve_and_compare_methods():
    A = np.array([[3, 1, -2], [2, -2, 4], [-1, 12, -1]], dtype=float)
    b = np.array([1, -2, 0], dtype=float)
    
    ge_solution, ge_time, ge_iters = gaussian_elimination(A.copy(), b.copy())
    jacobi_solution, jacobi_time, jacobi_iters = jacobi_method(A.copy(), b.copy())
    gs_solution, gs_time, gs_iters = gauss_seidel_method(A.copy(), b.copy())
    
    print("\nComparison of Methods:\n")
    print(f"{'Method':<15}{'x':<15}{'y':<15}{'z':<15}{'Time (s)':<15}{'Iterations':<10}")
    print("-" * 80)
    print(f"{'Gaussian':<15}{ge_solution[0]:<15.6g}{ge_solution[1]:<15.6g}{ge_solution[2]:<15.6g}{ge_time:<15.6f}{'-':<10}")
    print(f"{'Jacobi':<15}{jacobi_solution[0]:<15.6g}{jacobi_solution[1]:<15.6g}{jacobi_solution[2]:<15.6g}{jacobi_time:<15.6f}{jacobi_iters:<10}")
    print(f"{'Gauss-Seidel':<15}{gs_solution[0]:<15.6g}{gs_solution[1]:<15.6g}{gs_solution[2]:<15.6g}{gs_time:<15.6f}{gs_iters:<10}")

if __name__ == "__main__":
    solve_and_compare_methods()