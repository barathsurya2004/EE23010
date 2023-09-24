from scipy.stats import norm
from scipy.stats import binom
import numpy as np
from matplotlib import pyplot as plt
p = 0.25
n = 5
k = 0
sig = np.sqrt(n*p*(1-p))
print((((k-0.5)-n*p)/sig),((k+0.5)-n*p)/sig,((k)-n*p)/sig)
print("Probability from Gaussian approximation: ",norm.cdf(((k+0.5)-n*p)/sig)-norm.cdf((((k-0.5)-n*p)/sig)))
print("Probability from Binomial: ",(binom.pmf(k,n,p)))
mean = n*p
variance = np.sqrt(n*p*(1-p))

std_deviation = np.sqrt(variance)

k_values = np.arange(0, n + 1)

binom_pmf = binom.pmf(k_values, n, p)

x = np.linspace(mean - 3 * std_deviation, mean + 3 * std_deviation, 1000)

norm_pdf = norm.pdf(x, loc=mean, scale=std_deviation)

plt.figure(figsize=(10, 6))

plt.stem(k_values, binom_pmf, basefmt=' ', label=f'Binomial ')

plt.plot(x, norm_pdf, label=f'Normal', linewidth=2)

plt.xlabel('X (Number of Successes / X-values)')
plt.ylabel('Probability / Probability Density')
plt.title('Comparison of Binomial and Normal Distributions')
plt.xticks(k_values)
plt.legend()
plt.grid(True)
plt.show()