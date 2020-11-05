from math import erf
cdf = lambda x: 0.5 * (1 + erf ((x - mu) / (sigma * 2 ** 0.5) ))

mu, sigma = map(int, input().split(' '))
x1 = int(input())
x2 = int(input())

# You should output the percentage (not the probability) without the percent symbol.
print('{:.2f}'.format((1-cdf(x1))*100))
print('{:.2f}'.format((1-cdf(x2))*100))
print('{:.2f}'.format(cdf(x2)*100))