# y_hat = a + bx 
# Finding the value of b
# The value of b can be calculated using either of the following formulae:
# 1. b = (n sum(x_i * y_i) - sum(x_i) * sum(y_i)) / (n * sum(x_i^2) - (sum(x_i))^2)
# 2. b = rho sigma_y / sigma_x
# Finding the value of a
# a = y_bar - b x_bar
# Sums of squares
# Total sums of squares: SST = sum(y_i - y_bar)^2
# Regression sums of squares: SSR = sum(y_i_hat - y_bar)^2
# Error sums of squares: SSE = sum(y_i_hat - y_i)^2
# If SSE is small, we can assume that our fit is good.
# Coefficient of determination (R-squared)
# R^2 = SSR/SST = 1 - SSE/SST
# R^2 multiplied by 100 gives the percent of variation attributed to the linear regression between Y and X.

# * unpacks every item from a list (iterable) to a separate argument.
# zip(*p) passes all the items inside the p as arguments to the zip function.
n = 5
x, y = zip(*[map(int, input().split()) for i in range(n)])
sum_xy = sum([x*y for x, y in zip(x,y)])
b = (n * sum_xy - sum(x) * sum(y)) / (n * sum([x**2 for x in x]) - sum(x) ** 2)
a = sum(y)/n - b * sum(x)/n
print('{:.3f}'.format(a+b*80))