import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load data
iris = load_iris()
X = iris.data[:, :2]  # sepal length and width
y = iris.target
target_names = iris.target_names

# Stratified split 80/20
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.2, random_state=42
)

# Plot
plt.figure(figsize=(6, 6))
scatter = plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='viridis', edgecolor='k')
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.title("Figure 4a_PHAN TRAN THANH HUY_ITCSIU22056: Iris Classes (sepal length vs width)")
plt.grid(True)

# Colorbar legend
cbar = plt.colorbar(scatter, ticks=[0, 1, 2])
cbar.ax.set_yticklabels(target_names)
cbar.set_label('Iris class')

plt.show()
