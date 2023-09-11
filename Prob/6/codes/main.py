import scipy.stats as stats


n = 3 
p = 0.5  
X = stats.binom(n, p)
pmf_values = [X.pmf(k) for k in range(n + 1)]

for k, pmf in enumerate(pmf_values):
    print(f'P(X = {k}) = {pmf:.3f}')
