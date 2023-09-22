from scipy.stats import norm
from scipy.stats import binom
import numpy as np
from matplotlib import pyplot as plt

p = 0.05
n = 10
k = 1
sig = np.sqrt(n*p*(1-p))
print("Probability from Gaussian approximation: ",norm.cdf((k-n*p+0.5)/sig))
print("Probability from Binomial: ",(binom.cdf(k,n,p)))

n = 10
p = 0.05
sig = np.sqrt(n*p*(1-p))
k = np.linspace(0,n,n+1)
fig, ax = plt.subplots()
xpoints = k
ypoints = np.array(binom.pmf(k,n,p))
ax.stem(xpoints, ypoints,linefmt='r-', markerfmt='ro', basefmt='k--')
xpoints = np.linspace(-n,n,100*n)
ypoints = np.array(norm(n*p,sig).pdf(xpoints))
ax.plot(xpoints, ypoints,'b')
plt.legend(["Gaussian","Binomial"])
plt.xlabel("Number of Successes")
plt.ylabel("Probability")
plt.grid()
plt.show()