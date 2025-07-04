import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron

# Bước 1: Load Iris dataset
iris = load_iris()
X = iris.data[:, :2]  # Chỉ lấy 2 đặc trưng: sepal length và sepal width
y = iris.target
target_names = iris.target_names

# Bước 2: Lọc chỉ 2 lớp: Setosa (0) và Versicolor (1)
mask = y < 2
X_binary = X[mask]
y_binary = y[mask]

# Bước 3: Tách tập train/test theo tỉ lệ 80/20, stratify để cân bằng lớp
X_train, X_test, y_train, y_test = train_test_split(
    X_binary, y_binary, test_size=0.2, stratify=y_binary, random_state=42
)

# Bước 4: Vẽ scatter plot
plt.figure(figsize=(5, 5))
scatter = plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='viridis', edgecolor='k')
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.title("Figure 4b_PHAN TRAN THANH HUY_ITCSIU22056: Setosa vs Versicolor (Train Set)")
plt.grid(True)

# Bước 5: Colorbar (legend)
cbar = plt.colorbar(scatter, ticks=[0, 1])
cbar.ax.set_yticklabels(target_names[:2])  # Chỉ lấy tên của 2 lớp đầu
cbar.set_label('Iris class')

plt.show()

# (Optional) Bước 6: Huấn luyện Perceptron cho phân loại nhị phân
clf = Perceptron(random_state=0)
clf.fit(X_train, y_train)

# Đánh giá mô hình
train_acc = clf.score(X_train, y_train)
test_acc = clf.score(X_test, y_test)

print("Training accuracy:", train_acc)
print("Test accuracy:", test_acc)
print("Training error:", 1 - train_acc)
print("Test error:", 1 - test_acc)
