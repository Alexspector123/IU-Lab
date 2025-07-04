import math as m
import numpy as np
import matplotlib.pyplot as plt

def cos_T(x, terms):
    term = 0.0
    for i in range(terms):
        term += ((-1) ** i * x ** (2 * i)) / m.factorial(2 * i)
    return term

x=1
appro_cos = cos_T(x,4)
print(appro_cos)

x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 400)
y_actual_cos = np.cos(x_vals)
y_cos_4 = [cos_T(x, 4) for x in x_vals]

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_actual_cos, label="cos(x) actual", color='black')
plt.plot(x_vals, y_cos_4, label="Taylor Approximation (4 terms)", linestyle="dashed", color="blue")

plt.legend()
plt.xlabel("x")
plt.ylabel("cos(x)")
plt.title("Taylor Approximation of cos(x) with 4 terms")
plt.grid()
plt.show()