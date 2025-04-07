
import cupy as cp
import matplotlib.pyplot as plt

def monte_carlo_simulation(S0, mu, sigma, T, steps, simulations):
    dt = T / steps
    Z = cp.random.standard_normal((simulations, steps))
    S = cp.zeros((simulations, steps + 1))
    S[:, 0] = S0
    for t in range(1, steps + 1):
        S[:, t] = S[:, t-1] * cp.exp((mu - 0.5 * sigma**2) * dt + sigma * cp.sqrt(dt) * Z[:, t-1])
    return S

def plot_simulation(simulated_paths):
    plt.plot(cp.asnumpy(simulated_paths[:100, :]).T)
    plt.title("Monte Carlo Simulated Stock Paths")
    plt.xlabel("Days")
    plt.ylabel("Price")
    plt.show()
