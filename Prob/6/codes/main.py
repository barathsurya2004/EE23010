import math

def binomial_distribution(p, n, z):
  probabilities = []
  for k in range(n + 1):
    probabilities.append(math.comb(n,k)*(math.pow(p, k) * math.pow(1 - p, n - k)) * math.pow(z, k))

  return probabilities


p = 1/2
n = 3
z = 1

probabilities = binomial_distribution(p, n, z)

print("Probability of getting 3 heads:", probabilities[3])
print("Probability of getting 2 heads:", probabilities[2])
print("Probability of getting 1 head:", probabilities[1])
print("Probability of getting 0 heads:", probabilities[0])

