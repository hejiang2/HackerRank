# We use the following formula to calculate the Pearson correlation coefficient:
# rho_{X,Y} = sum(xi - mu_x)(yi - mu_y)/(n*sigma_x*sigma_y)

# list comprehension
# [thing for thing in list_of_things]

n = int(input())
x = list(map(float, input().split(' ')))
y = list(map(float, input().split(' ')))
mu_x = sum(x)/n
mu_y = sum(y)/n