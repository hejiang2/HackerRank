from math import erf
cdf = lambda x: .5 + .5 * erf((x - mu)/2 ** .5/sigma)
print(round(cdf(x1), 3))
print(round(cdf(x3) - cdf(x2), 3))
# Create a function for integration
# Calculate the area underneath a curve for a finite interval
# One method to compute integrals approximately, that a computer can actually handle, is done by filling the area of interest with a user-defined amount of rectangles of equal width and variable height then summing up all of the rectangle's areas.
# The Midpoint Rule:
# Each rectangle out of "N" rectangles has to have an equal width, Δx, but each nth rectangle cannot be the exact same: the varying factor is the height which varies as the function evaluated at a certain point. 
# The midpoint rule gets its name from the fact that you are evaluating the height of each rectangle as f(x_n), where "x_n" is the respective center-point of each rectangle, as apposed to the left or right of the rectangle. 
# Using the midpoint is like implementing an average which will make the approximation more accurate than if you were to use the right or left.
# The cumulative distribution function for a function with normal distribution is:
# phi(x) = 0.5 * (1 + erf((x - mu) / (sigma * 2 ** .5)))
# where erf is the error function:
# erf(z) = (2 / pi ** 0.5) * integration from 0 to 2 e ** (-x**2) dx

e = 2.71828
pi = 3.14159

def normal_pdf(x, mu, sigma):
    top = e**(-(x - mu)**2/(2*sigma**2))
    bottom = sigma*(2*pi)**0.5
    return top/bottom

def normal_cdf(a, b, n, mu, sigma):
    dx = float(b - a) / n
    area = 0
    midpoint = a + (dx / 2)
    for i in range(n):
        area += normal_pdf(midpoint, mu, sigma) * dx
        midpoint += dx
    return area

n = 10000
print(round(normal_cdf(0, 19.5, n, mu, sigma), 3))
print(round(normal_cdf(20, 22, n, mu, sigma), 3))