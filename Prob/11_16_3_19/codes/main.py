import random

def has_consecutive_numbers(lst):
    for i in range(len(lst) - 2):
        if lst[i] + 1 == lst[i + 1] and lst[i + 1] + 1 == lst[i + 2]:
            return True
    return False

num_trials = 100000 
count = 0 

for _ in range(num_trials):
    random_numbers = random.sample(range(1, 21), 3) 
    if has_consecutive_numbers(random_numbers):
        count += 1


probability = count / num_trials
required= 1-probability
print(f"Simulated Probability: {required:.4f}")

def calculate_combinations(n, k):
    # Calculate binomial coefficient C(n, k)
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    result = 1
    for i in range(1, min(k, n - k) + 1):
        result = result * (n - i + 1) // i
    return result

total_ways = calculate_combinations(20, 3) 

consecutive_ways = 18 

non_consecutive_ways = total_ways - consecutive_ways
theory=non_consecutive_ways/total_ways
print(f"Therotical probability: {theory:.4f}")


