
import httpx

NIM_API_KEY = "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"

def call_nim_llm(prompt: str) -> str:
    response = httpx.post(
        "https://integrate.api.nvidia.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {NIM_API_KEY}", "Content-Type": "application/json"},
        json={
            "model": "nvidia/nim-llama3-8b",
            "messages": [{"role": "user", "content": prompt}]
        }
    )
    return response.json()["choices"][0]["message"]["content"]
