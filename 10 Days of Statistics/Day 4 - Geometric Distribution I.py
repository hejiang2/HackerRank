# Negative Binomial Experiment
# A negative binomial experiment is a statistical experiment that has the following properties:
# 1. The experiment consists of n repeated trials.
# 2. The trials are independent.
# 3. The outcome of each trial is either success (s) or failure (f).
# 4. P(s) is the same for every trial.
# 5. The experiment continues until x successes are observed.
# If X is the number of experiments until the xth success occurs, then X is a discrete random variable called a negative binomial.

# Geometric Distribution
# The geometric distribution is a special case of the negative binomial distribution that deals with the number of Bernoulli trials required to get a success (i.e., counting the number of failures before the first success). 

numerator, denominator = map(float, input().split(' '))
first = int(input())

prob_defect = numerator / denominator
prob = (1 - prob_defect) ** (first - 1) * prob_defect
print('{:.3f}'.format(prob))