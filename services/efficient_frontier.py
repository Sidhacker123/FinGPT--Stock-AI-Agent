
import numpy as np
import matplotlib.pyplot as plt
import cvxpy as cp

def simulate_portfolios(returns, cov_matrix, num_portfolios=10000):
    results = []
    n_assets = len(returns)
    for _ in range(num_portfolios):
        weights = np.random.dirichlet(np.ones(n_assets), size=1)[0]
        port_return = np.dot(returns, weights)
        port_volatility = np.sqrt(weights.T @ cov_matrix @ weights)
        results.append((port_volatility, port_return, weights))
    return results

def plot_efficient_frontier(results, optimal_portfolio):
    vol, ret, _ = zip(*results)
    opt_vol, opt_ret, _ = optimal_portfolio
    plt.figure(figsize=(10,6))
    plt.scatter(vol, ret, c=ret, cmap="viridis", alpha=0.5)
    plt.plot(opt_vol, opt_ret, 'r*', markersize=15, label='Optimized Portfolio')
    plt.xlabel('Volatility (Risk)')
    plt.ylabel('Expected Return')
    plt.title('Efficient Frontier')
    plt.legend()
    plt.grid(True)
    plt.savefig("efficient_frontier.png")
    plt.close()
