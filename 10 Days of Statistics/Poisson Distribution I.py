# Poisson Experiment
# A Poisson experiment is a statistical experiment that has the following properties:

# 1. The outcome of each trial is either success or failure.
# 2. The average number of successes (lambda) that occurs in a specified region is known.
# 3. The probability that a success will occur is proportional to the size of the region.
# 4. The probability that a success will occur in an extremely small region is virtually zero.

# Poisson Distribution
# A Poisson random variable is the number of successes that result from a Poisson experiment. The probability distribution of a Poisson random variable is called a Poisson distribution:
# P(k, lambda) = lambda^k e^(-lambda) / k!
# Here,
# e = 2.71828
# lambda is the average number of successes that occur in a specified region.
# k is the actual number of successes that occur in a specified region.
# P(k, lambda) is the Poisson probability, which is the probability of getting exactly k successes when the average number of successes is lambda.

mean = input()
k = input()

e = 2.71828

def factorial(n):
    if n < 2:
        return 1
    else:
        return n*factorial(n-1)

def Poisson(k, mean):
    return (mean**k * e**(-mean))/factorial(k)

print(round(Poisson(int(k), float(mean)),3))