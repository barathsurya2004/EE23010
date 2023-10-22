import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Read the data from pois.dat
data = np.loadtxt("pois.dat")

# Sort the data in ascending order
data = np.sort(data)

# Calculate the empirical CDF
n = len(data)
cdf = np.arange(1, n + 1) / n

# Calculate the theoretical CDF using scipy's poisson distribution
l = 9  # Change this to your desired mean
x = np.arange(0, np.max(data) + 1)
theoretical_cdf = poisson.cdf(x, l)

# Plot the empirical CDF and theoretical CDF with a scatter plot
plt.step(data, cdf, label="Empirical CDF")
plt.scatter(x, theoretical_cdf, color='red', marker='x')
plt.plot(x,theoretical_cdf,label="Theoretical CDF (Poisson)",color='red')
plt.xlabel("X")
plt.ylabel("CDF")
plt.title("Empirical vs. Theoretical CDF of Poisson Distribution")
plt.legend()
plt.grid()
plt.show()
