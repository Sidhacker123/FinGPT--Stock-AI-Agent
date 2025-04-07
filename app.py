
from fastapi import FastAPI
from agent.fin_agent import FinGPT

app = FastAPI()
agent = FinGPT()

@app.get("/ask")
def ask(q: str):
    return agent.ask(q)
