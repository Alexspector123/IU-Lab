import numpy as np
import matplotlib.pyplot as plt
from math import log
from scipy.integrate import quad

def f(x):
    return np.log(x)

def simpson_13(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be even for Simpson's 1/3 Rule")
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    result = y[0] + y[-1] + 4 * sum(y[1:-1:2]) + 2 * sum(y[2:-2:2])
    return (h / 3) * result

a, b = 1, 2
exact, _ = quad(f, a, b)

ns = [2, 4, 6, 8]
approximations = []
relative_errors = []

for n in ns:
    approx = simpson_13(f, a, b, n)
    rel_error = abs((approx - exact) / exact)
    approximations.append(approx)
    relative_errors.append(rel_error)

print(f"{'n':<5}{'Approximation':<20}{'Relative Error':<20}")
print("-" * 45)
for n, approx, err in zip(ns, approximations, relative_errors):
    print(f"{n:<5}{approx:<20.10f}{err:<20.10f}")

log_n = np.log10(ns)
log_error = np.log10(relative_errors)

plt.figure(figsize=(8, 5))
plt.plot(log_n, log_error, marker='o', linestyle='-', color='teal')
plt.title("log(Relative Error) vs log(n) for Simpson's 1/3 Rule")
plt.xlabel("log(n)")
plt.ylabel("log(Relative Error)")
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
