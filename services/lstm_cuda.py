
import torch
import torch.nn as nn
import numpy as np

# CUDA-Powered LSTM Model
class LSTMModel(nn.Module):
    def __init__(self, input_size=1, hidden_size=64, num_layers=2, output_size=1):
        super(LSTMModel, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out, _ = self.lstm(x)
        out = self.fc(out[:, -1, :])
        return out

def train_lstm_on_returns(returns):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    window = 30
    X, y = [], []
    for i in range(len(returns) - window):
        X.append(returns[i:i + window])
        y.append(returns[i + window])
    X = np.array(X)
    y = np.array(y)
    X_tensor = torch.tensor(X[:, :, None], dtype=torch.float32).to(device)
    y_tensor = torch.tensor(y[:, None], dtype=torch.float32).to(device)

    model = LSTMModel().to(device)
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    for epoch in range(30):
        output = model(X_tensor)
        loss = criterion(output, y_tensor)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    return model
