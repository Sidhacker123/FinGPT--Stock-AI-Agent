This project showcases:

Multi-agent LLM orchestration

Enterprise RAG + financial logic

Live NeMo + NIM integration

CUDA-enhanced modeling

# Agentic Fintech AI System

This project is a multi-agent financial assistant powered by NVIDIA NIM, CUDA, LSTM-based forecasting, and portfolio optimization logic. It includes:

- 📊 Portfolio generation agent using LSTM and Modern Portfolio Theory (MPT), simulations of 10k+ portfolio through Monte-Carlo leveraging CUDA 
- 💸 Loan restructuring agent with FOIR and DSCR evaluation
- 🧠 NeMo + NIM API integration for reasoning and explanations
- 🌐 Streamlit UI and FastAPI backend
- 💾 Alpha Vantage API integration for real-time stock data

Component	Description
🧠 Custom RAG	FAISS-based fallback for fast offline document embedding & retrieval
🌐 NVIDIA NeMo Retriever	Live document retrieval via nvidia/nim-rag-retriever-mixtral, with logs in logs/rag_live_*.json
🧮 CUDA-LSTM Models	PyTorch models accelerated with CUDA to forecast asset returns and simulate portfolio risk
🧠 PortfolioAgent & DebtAgent	Modular, smart agents with reasoning, planning, execution, and self-critique capabilities
🤖 NIM-powered Reasoning	Calls nvidia/nim-llama3-8b for explanation generation, rationale validation, and critiques
📊 Alpha Vantage Integration	Real-time financial data for price/return fetching and evaluator scoring
🔐 Streamlit UI + Auth	Login-secured web app to upload PDFs/CSVs, ask financial questions, and run agents
🔁 Session Logs + Markdown Export	Session histories stored and exportable for compliance, review, or investor reports
📬 Email Notifications	Auto-email weekly NeMo Retriever insights to investor inboxes
🧪 NeMo Evaluator (planned)	Evaluation of agent responses for factuality, clarity, and reasoning (API pending)

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

🔍 RAG Pipeline
Mode	                         Source	                        Output
⚡ Online(Live)	               NeMo Retriever (Mixtral)	   Retrieves news/filings in real-time
🗃️ Offline(Fallback)	         FAISS local index	         Pulls from embedded PDFs and CSVs
✅ Logging           	         logs/rag_live_*.json	       Audit trails of all RAG executions


🔄 Model Training + Inference
LSTM models trained on historical return data
Optimized with CUDA backend for faster epochs
Deployment-ready with TorchScript/ONNX support
Monte Carlo simulations & efficient frontiers auto-generated

📧 Auto Insights (Investor Mode)
Weekly script uses NeMo Retriever to pull:
“Top 10 AI stocks this week”
“Emerging semiconductor risks”
Auto-emails summary to siddpurdue@gmail.com
Logs saved to logs/ for historical insight

🧪 NeMo Evaluator (Planned Integration)
Will score agent responses on:
Accuracy vs Alpha Vantage ground truth
Reasoning completeness
Clarity & relevance for decision making

🧠 Role of NIM API in This System
Component	NIM Contribution
📜 LLM reasoning	Turns dry allocation data into rich explanations
📚 Retriever	Adds market context to justify allocation decisions
🤖 Agent Evaluation	(Optional) Self-critiquing agents via trajectory feedback
✅ NIM = Human-like intelligence layer over your structured ML logic

Trade-Offs between Custom RAG and Nemo Retriever
Feature	FAISS                            (Custom RAG)   	NeMo Retriever
Offline support	                               ✅	          ❌ (API-only)
No rate limits	                               ✅     	    ❌
Custom data (PDF/CSV uploads)                  ✅	          ❌
Scales with GPU infra	                         ✅         	Limited
Real-time cloud news	                         ❌   	      ✅
Secure hosted source (Bloomberg, SEC)	         ❌	          ✅
So I decided to use both of them in this project

FUTURE-
Working on enhancing the RAG & Nemo Evaluator



