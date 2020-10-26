# Central Limit Theorem
# The central limit theorem (CLT) states that, for a large enough sample (n), the distribution of the sample mean will approach normal distribution. This holds for a sample of independent random variables from any distribution with a finite standard deviation.
# Let {X1, X2, X3, ..., Xn} be a random data set of size n, that is, a sequence of independent and identically distributed random variables drawn from distributions of expected values given by mu and finite variances given by sigma^2. 
# For large n, the distribution of sample sums Sn is close to normal distribution (mu', sigma') where:
# mu' = n * mu
# sigma' = n ** 0.5 * sigma

max_pound = int(input())
num_boxes = int(input())
mu = int(input())
sigma = int(input())

mu_prime = mu * num_boxes
sigma_prime = sigma * num_boxes ** 0.5

from math import erf
cdf = lambda x: 0.5 * (1 + erf((x - mu_prime) / (sigma_prime * 2 ** .5)))
print('{:.4f}'.format(cdf(max_pound)))