# Recall that if a random variable has a Poisson distribution, then:
# E(X) = lambda
# Var(X) = lambda
# E(X^2) = lambda + lambda^2

A_mean, B_mean = map(float, input().split(' '))

print(round(160 + 40 * (A_mean + A_mean**2), 3))
print(round(128 + 40 * (B_mean + B_mean**2), 3))
