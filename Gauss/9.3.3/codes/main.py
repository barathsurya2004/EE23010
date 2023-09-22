import numpy as np

def simulate_sample_numpy(prob_defective, sample_size, num_simulations):
    samples = np.random.choice([0, 1], size=(num_simulations, sample_size), p=[1 - prob_defective, prob_defective])
    num_defective = np.sum(samples, axis=1)
    num_successes = np.sum(num_defective <= 1)
    
    probability = num_successes / num_simulations
    return probability

# Parameters
prob_defective = 0.05  # 5% defective items
sample_size = 10       # Size of the sample
num_simulations = 100000  # Number of simulations

result = simulate_sample_numpy(prob_defective, sample_size, num_simulations)
print(f"simulated probability of not more than one defective item: {result:.4f}")

