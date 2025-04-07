
import os
import toml
import httpx
import json

# Load API key from secrets
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "../configs/secrets.toml")
config = toml.load(CONFIG_PATH)
API_KEY = config.get("NVIDIA", {}).get("NIM_API_KEY", "")

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Call NVIDIA NIM LLM for reasoning
async def run_nim_llm(prompt: str) -> str:
    url = "https://integrate.api.nvidia.com/v1/chat/completions"
    payload = {
        "model": "nvidia/nim-llama3-8b",
        "messages": [
            {"role": "system", "content": "You are a financial advisor AI."},
            {"role": "user", "content": prompt}
        ]
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=HEADERS, json=payload)
        result = response.json()
        message = result.get("choices", [{}])[0].get("message", {}).get("content", "No response from LLM.")
        with open("logs/llm_output.txt", "w") as f:
            f.write(message)
        return message

# NeMo Retriever: document search (RAG)
async def retrieve_docs(query: str) -> list:
    url = "https://integrate.api.nvidia.com/v1/retrieval/query"
    payload = {
        "query": query,
        "retriever": "nvidia/nim-rag-retriever-mixtral"
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=HEADERS, json=payload)
        result = response.json()
        docs = [doc["content"] for doc in result.get("documents", [])]
        with open("logs/rag_docs.json", "w") as f:
            json.dump(docs[:3], f, indent=4)
        return docs[:2] if docs else ["No docs found."]

# NeMo Evaluator: simulate LLMOps evaluation of reasoning or plan
def evaluate_trajectory(agent_output: dict) -> dict:
    # Mock evaluation logic — later connect to real NeMo Evaluator if public endpoint is available
    import random
    result = {
        "accuracy_score": round(random.uniform(0.7, 0.95), 2),
        "reasoning_score": round(random.uniform(0.6, 0.9), 2),
        "explanation": "Evaluation complete based on synthetic scoring."
    }
    with open("logs/evaluator_output.json", "w") as f:
        json.dump(result, f, indent=4)
    return result
