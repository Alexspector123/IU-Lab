import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.linear_model import Perceptron
from sklearn.multiclass import OneVsRestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dữ liệu Iris (chỉ lấy 2 features đầu tiên để dễ vẽ)
iris = datasets.load_iris()
X = iris.data[:, :2]
y = iris.target

# Chia dữ liệu train/test, đảm bảo cân bằng lớp
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.2, random_state=42
)

# Tạo One-vs-All classifier với Perceptron
ova_clf = OneVsRestClassifier(Perceptron(max_iter=1000, random_state=0))
ova_clf.fit(X_train, y_train)

# Dự đoán train và test
y_train_pred = ova_clf.predict(X_train)
y_test_pred = ova_clf.predict(X_test)

print("Train accuracy:", accuracy_score(y_train, y_train_pred))
print("Test accuracy:", accuracy_score(y_test, y_test_pred))

# --- Vẽ trực quan ranh giới quyết định ---

# Tạo lưới điểm để dự đoán
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))

Z = ova_clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.figure(figsize=(10, 6))
plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.Set1)

# Vẽ điểm dữ liệu train và test
colors = ['red', 'green', 'blue']
labels = iris.target_names

for i, color, label in zip(range(3), colors, labels):
    plt.scatter(X_train[y_train == i, 0], X_train[y_train == i, 1],
                color=color, edgecolor='k', label=f'Train {label}')
    plt.scatter(X_test[y_test == i, 0], X_test[y_test == i, 1],
                color=color, edgecolor='k', alpha=0.5, label=f'Test {label}')

plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.title("Phan Tran Thanh Huy_ITCSIU22056_One-vs-All classification with Perceptron on Iris dataset")
plt.legend()
plt.show()
