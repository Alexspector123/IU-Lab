# Given data points
x_values = [1, 2, 4, 7]
y_values = [3, 6, 10, 20]

def newton_divided_diff(x, y):
    n = len(x)
    table = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        table[i][0] = y[i]
    
    for j in range(1, n):
        for i in range(n - j):
            numerator = table[i + 1][j - 1] - table[i][j - 1]
            denominator = x[i + j] - x[i]
            table[i][j] = numerator / denominator
    
    coeffs = [table[0][j] for j in range(n)]
    return coeffs, table

def newton_polynomial(x_data, coeffs, x):
    n = len(coeffs)
    result = coeffs[0]
    product_term = 1.0
    for i in range(1, n):
        product_term *= (x - x_data[i - 1])
        result += coeffs[i] * product_term
    return result

# Step 1: Get coefficients using divided differences (with dynamic programming)
coefficients, table = newton_divided_diff(x_values, y_values)

# Step 2: Estimate f(3)
x_to_estimate = 3
estimated_value = newton_polynomial(x_values, coefficients, x_to_estimate)

# Output results
print(f"Estimated f({x_to_estimate}) using Newton interpolation: {estimated_value:.6f}")