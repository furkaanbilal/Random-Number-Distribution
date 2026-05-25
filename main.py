import random

# Number of random values to generate
trials = 100

# Store results
results = {}

# Generate random numbers from 1 to 10
for _ in range(trials):
    number = random.randint(1, 10)

    if number in results:
        results[number] += 1
    else:
        results[number] = 1

# Display results
print("Random Number Distribution:\n")

for number in sorted(results):
    print(f"{number}: {results[number]}")
