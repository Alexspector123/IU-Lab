import numpy as np
import matplotlib.pyplot as plt
import math as m

def taylor_sin(x, terms):
    taylor_series = 0
    for i in range(terms):
        term = ((-1)**i * x**(2*i+1)) / m.factorial(2*i+1)
        taylor_series += term
    return taylor_series

x=1

approximation = taylor_sin(x, 4)
print(approximation)

x_vals = np.linspace(-2*np.pi, 2*np.pi, 400)
y_actual = np.sin(x_vals)

y_approx_1 = [taylor_sin(x, 1) for x in x_vals]
y_approx_3 = [taylor_sin(x, 3) for x in x_vals]
y_approx_5 = [taylor_sin(x, 5) for x in x_vals]

plt.figure(figsize=(10, 5))
plt.plot(x_vals, y_actual, label='sin(x)', color='black')
plt.plot(x_vals, y_approx_1, label='1-term Taylor', linestyle='dashed')
plt.plot(x_vals, y_approx_3, label='3-term Taylor', linestyle='dotted')
plt.plot(x_vals, y_approx_5, label='5-term Taylor', linestyle='dashdot')

plt.legend()
plt.xlabel('x')
plt.ylabel('sin(x) and Approximations')
plt.title('Taylor Series Approximation of sin(x)')
plt.grid()
plt.show()