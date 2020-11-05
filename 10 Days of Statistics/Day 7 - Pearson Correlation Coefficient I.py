# We use the following formula to calculate the Pearson correlation coefficient:
# rho_{X,Y} = sum(xi - mu_x)(yi - mu_y)/(n*sigma_x*sigma_y)

# list comprehension
# [thing for thing in list_of_things]
# List comprehension is an elegant way to define and create list in Python. 

# input().split(separator, maxsplit)
n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))
mu_x = sum(x)/n
mu_y = sum(y)/n

var_x = sum([(x - mu_x)**2 for x in x])/n
var_y = sum([(y - mu_y)**2 for y in y])/n

std_x = var_x**0.5
std_y = var_y**0.5

# The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
# If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.

cov = sum([(x - mu_x) * (y - mu_y) for x, y in zip(x, y)])
corr = cov / (n * std_x * std_y)
print('{:.3f}'.format(corr))