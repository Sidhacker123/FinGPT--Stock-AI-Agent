
# Agentic Fintech AI System

This project is a multi-agent financial assistant powered by NVIDIA NIM, CUDA, LSTM-based forecasting, and portfolio optimization logic. It includes:

- 📊 Portfolio generation agent using LSTM and Modern Portfolio Theory (MPT)
- 💸 Loan restructuring agent with FOIR and DSCR evaluation
- 🧠 NeMo + NIM API integration for reasoning and explanations
- 🌐 Streamlit UI and FastAPI backend
- 💾 Alpha Vantage API integration for real-time stock data

## Setup Instructions

### 1. Clone this repository

### 2. Install dependencies on a GPU server
```bash
bash gpu_setup.sh
```

### 3. Add your API keys in `configs/secrets.toml`
```toml
[NVIDIA]
NIM_API_KEY = "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"

[ALPHA_VANTAGE]
API_KEY = "NXJNBRRG8FGKS7TN"
```

### 4. Run backend + UI
```bash
uvicorn main:app --reload
streamlit run app.py
```

## Agent Descriptions

### Portfolio Agent
- Uses LSTM to predict stock return
- Applies volatility-based scoring
- Optimizes allocation using MPT
- Explains strategy with NeMo LLM

### Loan Restructuring Agent
- Parses user debts
- Calculates DSCR and FOIR
- Generates restructuring suggestions with LLM
