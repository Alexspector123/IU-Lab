import numpy as np
import matplotlib.pyplot as plt
import math as m

def taylor_sin(x, terms):
    taylor_series = 0
    for i in range(terms):
        term = ((-1)**i * x**(2*i+1)) / m.factorial(2*i+1)
        taylor_series += term
    return taylor_series

x_vals = np.linspace(-2*np.pi, 2*np.pi, 400)
y_actual = np.sin(x_vals)

y_approx_5 = np.array([taylor_sin(x, 5) for x in x_vals])

absolute_error = np.abs(y_actual - y_approx_5)

plt.figure(figsize=(10, 5))
plt.plot(x_vals, absolute_error, label = 'Absolute Error (5 terms)', color='red', linewidth=2)

plt.legend()
plt.xlabel('x')
plt.ylabel('Absolute Error')
plt.title('Absolute Error of Taylor Series Approximation for sin(x) (5 terms)')
plt.grid()
plt.show()