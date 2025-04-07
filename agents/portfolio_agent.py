
import numpy as np
import cvxpy as cp
from services.alpha_vantage import get_stock_data
from services.lstm_cuda import LSTMModel, train_lstm_on_returns
from services.model_utils import save_model, load_model
from services.efficient_frontier import simulate_portfolios, plot_efficient_frontier
from services.llmops_nemo import run_nim_llm
from models.schemas import UserRequest, AIResponse

async def generate_portfolio(user_input: UserRequest) -> AIResponse:
    stock_data = await get_stock_data(sector="tech", risk=user_input.risk_tolerance)
    returns = []
    volatilities = []
    symbols = []

    for stock in stock_data:
        symbol = stock['symbol']
        # Simulated returns for LSTM training
        stock_returns = np.random.randn(1000) * 0.01
        model = train_lstm_on_returns(stock_returns)
        save_model(model, symbol)
        predicted_return = float(model(torch.tensor(stock_returns[-30:].reshape(1, 30, 1)).float().cuda()).item())
        stock['predicted_return'] = predicted_return
        stock['volatility'] = np.std(stock_returns)
        returns.append(predicted_return)
        volatilities.append(stock['volatility'])
        symbols.append(symbol)

    if not returns:
        return AIResponse(summary="No valid stock data available.", actions=[], data={})

    # Portfolio Optimization (MPT)
    n = len(returns)
    weights = cp.Variable(n)
    expected_returns = np.array(returns)
    cov_matrix = np.diag(np.array(volatilities)**2)
    objective = cp.Maximize(expected_returns @ weights - 0.5 * cp.quad_form(weights, cov_matrix))
    constraints = [cp.sum(weights) == 1, weights >= 0]
    prob = cp.Problem(objective, constraints)
    prob.solve()
    final_weights = weights.value

    selected = []
    actions = []
    for i, symbol in enumerate(symbols):
        allocation = round(final_weights[i] * 100, 2)
        if allocation > 0:
            selected.append({
                "symbol": symbol,
                "allocation_%": allocation,
                "predicted_return": round(returns[i], 4),
                "volatility": round(volatilities[i], 4)
            })
            actions.append(f"Allocate {allocation}% to {symbol} (Return: {round(returns[i], 4)}, Volatility: {round(volatilities[i], 4)})")

    portfolios = simulate_portfolios(expected_returns, cov_matrix)
    plot_efficient_frontier(portfolios, (np.sqrt(final_weights @ cov_matrix @ final_weights), np.dot(expected_returns, final_weights), final_weights))

    prompt = f"Explain the reasoning for creating a portfolio with these assets: {selected} for a {user_input.risk_tolerance}-risk investor with goals {user_input.goals}."
    llm_reasoning = await run_nim_llm(prompt=prompt)
    summary = f"Optimized a {user_input.risk_tolerance}-risk portfolio using MPT.\nLLM Explanation: {llm_reasoning}"

    return AIResponse(summary=summary, actions=actions, data={"portfolio": selected})
