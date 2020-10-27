# Standard scores are most commonly called z-scores.
# In statistics, the standard score is the number of standard deviations by which the value of a raw score (i.e., an observed value or data point) is above or below the mean value of what is being observed or measured. Raw scores above the mean have positive standard scores, while those below the mean have negative standard scores.
# Suppose X1, X2, ..., Xn are n independent random variables with means mu_1, mu_2, ..., mu_n and variances sigma_1^2, sigma_2^2, ..., sigma_n^2. Then, the mean and the variance of the linear combination Y = sum a_i X_i where a1, a2, ..., an are real constants are:
# mu_y = sum a_i mu_i 
# and
# sigma_y^2 = sum a_i^2 sigma_i^2
# respectively.

# Mean and Variance of Sample Mean
# E(X_bar) = mu
# Var(X_bar) = sigma^2/n
# upper limit = sample_mean + z-score * sample_sd
# lower limit = sample_mean - z-score * sample_sd

from math import sqrt

n = int(input())
mu = int(input())
sigma = int(input())
interval = float(input())
z = float(input())
print(round(mu - (sigma / sqrt(n)) * z, 2))
print(round(mu + (sigma / sqrt(n)) * z, 2))