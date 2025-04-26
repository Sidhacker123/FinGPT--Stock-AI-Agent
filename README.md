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

# 1. Install dependencies

pip install -r requirements.txt

# 2. Add API keys

configs/secrets.toml

# 3. Embed docs (optional)

python -m rag.faiss_retriever

# 4. Run the Streamlit UI

streamlit run streamlit_app.py

# 5. Run FastAPI backend

uvicorn app:app --reload


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

Mode	                                                                                             Source	                                             Output

⚡ Online(Live)	                                                                        NeMo Retriever (Mixtral)	                         Retrieves news/filings in real-time

🗃️ Offline(Fallback)	                                                                       FAISS local index	                            Pulls from embedded PDFs and CSVs

✅ Logging           	                                                                     logs/rag_live_*.json	                            Audit trails of all RAG executions


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

Accuracy vs Alpha Vantage real time truth

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

🔹 Architecture Diagram: FinGPT System Architecture

Overview:
FinGPT is an enterprise-grade multi-agent AI system for financial portfolio generation, credit optimization, and real-time investor recommendations. It leverages distributed computing to provide scalable, low-latency responses using multiple NVIDIA technologies.

System Components:

Client Layer

Web UI (Streamlit)

REST API (FastAPI)

User auth, stock search, portfolio configuration

Controller Service

Agent Orchestration Layer

Task Dispatcher (PortfolioAgent, DebtAgent, ShadowInvestorAgent)

Agent Layer (Multi-agent System)

PortfolioAgent: Uses LSTM + Monte Carlo + cvxpy

DebtAgent: Uses FOIR/DSCR + Restructuring Planner

ShadowInvestorAgent: Leverages strategy mimicry using RL

Data & Retrieval Layer

Real-time stock feed via Alpha Vantage

Knowledge base with NVIDIA NeMo Retriever

FAISS fallback for offline RAG

LLMOps Layer

Model store (CUDA-accelerated PyTorch models)

Feedback capture pipeline (RAG + User Labels)

Evaluation framework for agent consistency, hallucination check

Infrastructure Layer

Distributed inference using NVIDIA NIM APIs

Task queues via Redis

Compute orchestration using Docker + NVIDIA Docker runtime

🔹 LLMOps Workflow: Pipeline & Retrieval Logic

Workflow Steps:

Input Prompt (User stock/portfolio query)

RAG Engine Routing:

NeMo Retriever fetches context

If offline, fallback to FAISS

Agent Activation:

Controller dispatches task to PortfolioAgent or DebtAgent

CUDA Inference:

CUDA-based PyTorch model runs LSTM predictions

Strategy Generation:

Output goes through explanation generator using NIM LLaMA3-8B

Feedback Capture:

User rates recommendation (used for retraining signal)

🔹 Distributed Computing Highlights

Multi-node Inference: PortfolioAgent and DebtAgent inference requests distributed across GPU nodes

Parallelism: Training LSTM models using data parallel PyTorch on multiple CUDA cores

LLM Serving: NeMo Retriever and LLaMA3 inference distributed across NIM endpoint replicas

Fault Tolerance: Redis queues with retry logic; fallback FAISS search node

Observability: Logs, metrics, and evaluation scores pushed to Prometheus/Grafana



