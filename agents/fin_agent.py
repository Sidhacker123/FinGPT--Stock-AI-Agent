
from rag.rag_pipeline import rag_answer
from datetime import datetime

class FinGPT:
    def __init__(self):
        self.history = []

    def ask(self, query):
        response = rag_answer(query)
        self.history.append({
            "timestamp": datetime.now().isoformat(),
            "query": query,
            "answer": response["answer"],
            "sources": response["docs"]
        })
        return response

    def get_history(self):
        return self.history

    def export_history(self, filepath="logs/session_history.json"):
        import json, os
        os.makedirs("logs", exist_ok=True)
        with open(filepath, "w") as f:
            json.dump(self.history, f, indent=4)
