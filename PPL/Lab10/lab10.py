# Recreate the comparison code between Perceptron and RL on Iris dataset
#example_code = 
#Example: Comparing Perceptron vs Reinforcement Learning (Q-Learning) for Binary Classification
#Dataset: Iris (Setosa vs Versicolor)
#Features: Sepal length and Sepal width

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, precision_score, recall_score
import gym
from gym import spaces

iris = load_iris()
X = iris.data[:, :2]
y = iris.target
mask = y < 2
X_binary = X[mask]
y_binary = y[mask]

X_train, X_test, y_train, y_test = train_test_split(
    X_binary, y_binary, test_size=0.2, stratify=y_binary, random_state=42)

# Perceptron
perceptron = Perceptron(max_iter=1000, eta0=0.1, random_state=42)
perceptron.fit(X_train, y_train)
y_pred_p = perceptron.predict(X_test)

# RL setup
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
kmeans = KMeans(n_clusters=20, random_state=42, n_init=10)
kmeans.fit(X_train_scaled)

class IrisEnv(gym.Env):
    def __init__(self, X, y):
        super(IrisEnv, self).__init__()
        self.X = X
        self.y = y
        self.current = 0
        self.observation_space = spaces.Box(low=np.min(X), high=np.max(X), shape=(2,), dtype=np.float32)
        self.action_space = spaces.Discrete(2)

    def reset(self):
        self.current = 0
        return self.X[self.current]

    def step(self, action):
        label = self.y[self.current]
        reward = 1 if action == label else -1
        self.current += 1
        done = self.current >= len(self.X)
        obs = self.X[self.current] if not done else np.zeros(2)
        return obs, reward, done, {}

class QAgent:
    def __init__(self, n_states, n_actions, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.q_table = np.zeros((n_states, n_actions))
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.n_actions = n_actions

    def choose_action(self, state_idx):
        if np.random.rand() < self.epsilon:
            return np.random.randint(self.n_actions)
        return np.argmax(self.q_table[state_idx])

    def update(self, s, a, r, s_next):
        best_next = np.max(self.q_table[s_next])
        self.q_table[s, a] += self.alpha * (r + self.gamma * best_next - self.q_table[s, a])

env = IrisEnv(X_train_scaled, y_train)
agent = QAgent(n_states=20, n_actions=2)

for ep in range(30):
    obs = env.reset()
    state = kmeans.predict([obs])[0]
    done = False
    while not done:
        action = agent.choose_action(state)
        next_obs, reward, done, _ = env.step(action)
        next_state = kmeans.predict([next_obs])[0]
        agent.update(state, action, reward, next_state)
        state = next_state

X_test_scaled = scaler.transform(X_test)
rl_preds = [agent.choose_action(kmeans.predict([obs])[0]) for obs in X_test_scaled]

print("Perceptron Accuracy:", accuracy_score(y_test, y_pred_p))
print("RL Agent Accuracy: ", accuracy_score(y_test, rl_preds))
print("RL Precision: ", precision_score(y_test, rl_preds, zero_division=0))
print("RL Recall: ", recall_score(y_test, rl_preds, zero_division=0))

plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.title("Perceptron Decision Boundary")
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred_p, cmap='coolwarm', edgecolor='k')
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

plt.subplot(1, 2, 2)
plt.title("RL Agent Decision (Test Data)")
plt.scatter(X_test[:, 0], X_test[:, 1], c=rl_preds, cmap='coolwarm', edgecolor='k')
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.tight_layout()
plt.show(block=True)