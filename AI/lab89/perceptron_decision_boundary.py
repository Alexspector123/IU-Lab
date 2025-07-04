import numpy as np
import matplotlib.pyplot as plt

# Hàm kích hoạt Heaviside step
def perceptron_output(x, w, b):
    z = np.dot(w, x) + b
    return 1 if z >= 0 else 0

# Trọng số và bias
w = np.array([1.0, 1.0])  # w1 = w2 = 1
b = -2.0  # bias để dịch chuyển ranh giới

# Tạo lưới điểm trên không gian (x1, x2)
x1_vals = np.linspace(-5, 5, 300)
x2_vals = np.linspace(-5, 5, 300)
X1, X2 = np.meshgrid(x1_vals, x2_vals)
Z = np.zeros_like(X1)

# Tính đầu ra perceptron tại mỗi điểm trên lưới
for i in range(X1.shape[0]):
    for j in range(X1.shape[1]):
        x = np.array([X1[i, j], X2[i, j]])
        Z[i, j] = perceptron_output(x, w, b)

# Vẽ vùng quyết định
plt.figure(figsize=(6, 6))
plt.contourf(X1, X2, Z, levels=[-0.1, 0.5, 1.1], colors=['white', 'skyblue'], alpha=0.7)
plt.contour(X1, X2, Z, levels=[0.5], colors='black', linewidths=2)

# Vẽ các trục
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

# Nhãn trục và cài đặt hiển thị
plt.xlabel("$x_1$")
plt.ylabel("$x_2$")
plt.grid(True)
plt.title("Perceptron Decision Boundary and Regions")
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.show()
