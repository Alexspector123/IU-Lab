import torch
import torch.nn as nn

class PolicyNetwork(nn.Module):
    def __init__(self, input_dim, hidden_dim=64):
        super(PolicyNetwork, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 2)  # 2 outputs: ham or spam
        )

    def forward(self, x):
        return self.net(x)