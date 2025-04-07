
import httpx
import toml
import os
import json
from datetime import datetime

config = toml.load("configs/secrets.toml")
API_KEY = config["NVIDIA"]["NIM_API_KEY"]

def live_retrieve(query: str, top_k=3) -> list:
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    url = "https://integrate.api.nvidia.com/v1/retrieval/query"
    payload = {
        "query": query,
        "retriever": "nvidia/nim-rag-retriever-mixtral"
    }

    try:
        r = httpx.post(url, headers=headers, json=payload)
        r.raise_for_status()
        results = r.json().get("documents", [])[:top_k]
        log = {
            "timestamp": datetime.utcnow().isoformat(),
            "query": query,
            "documents": results
        }
        os.makedirs("logs", exist_ok=True)
        with open(f"logs/rag_live_{datetime.now().strftime('%Y%m%d_%H%M')}.json", "w") as f:
            json.dump(log, f, indent=4)
        return results
    except Exception as e:
        return [{"error": str(e)}]
