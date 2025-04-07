
from fastapi import FastAPI
from agents.portfolio_agent import generate_portfolio
from agents.debt_agent import restructure_debt
from models.schemas import UserRequest, AIResponse

app = FastAPI()

@app.post("/generate_portfolio", response_model=AIResponse)
async def portfolio_endpoint(user_input: UserRequest):
    return await generate_portfolio(user_input)

@app.post("/restructure_debt", response_model=AIResponse)
async def debt_endpoint(user_input: UserRequest):
    return await restructure_debt(user_input)
