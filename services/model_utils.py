
import torch
import os

def save_model(model, symbol):
    os.makedirs("models", exist_ok=True)
    path = f"models/lstm_{symbol}.pt"
    torch.save(model.state_dict(), path)

def load_model(model_class, symbol):
    path = f"models/lstm_{symbol}.pt"
    model = model_class()
    if os.path.exists(path):
        model.load_state_dict(torch.load(path))
        model.eval()
    return model
