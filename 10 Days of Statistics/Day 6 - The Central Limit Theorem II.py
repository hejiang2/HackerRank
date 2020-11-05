tickets = int(input())
students = int(input())
mu = float(input())
sigma = float(input())

mu_prime = mu * students
sigma_prime = sigma * students ** 0.5

from math import erf
cdf = lambda x: 0.5 * (1 + erf((x - mu_prime) / (sigma_prime * 2 ** .5)))
print('{:.4f}'.format(cdf(tickets)))