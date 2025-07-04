import numpy as np

def f(A, b, x):
    return np.dot(A, x) - b

def forward_elimination(A, b):
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
    return A, b

def backward_substitution(A, b):
    n = len(A)
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    return x

def gaussian_elimination(A, b):
    A, b = forward_elimination(A, b)
    return backward_substitution(A, b)

def solve_linear_system():
    A = np.array([[3, 1, -2], [2, -2, 4], [-1, 12, -1]], dtype=float)
    b = np.array([1, -2, 0], dtype=float)
    solution = gaussian_elimination(A, b)
    print(f"\nApproximate solution:\n x = {solution[0]}\n y = {solution[1]}\n z = {solution[2]}")

if __name__ == "__main__":
    solve_linear_system()