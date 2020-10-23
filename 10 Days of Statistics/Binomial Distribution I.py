# map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
boy, girl = map(float, input().split(' '))
p_boy = boy / (boy + girl)

# Recursive functions in Python
# Recursion is a way of programming or coding a problem, in which a function calls itself one or more times in its body. 
# Usually, it is returning the return value of this function call. 
# Termination condition:
# A recursive function has to terminate to be used in a program. 
# A recursive function terminates, if with every recursive call the solution of the problem is downsized and moves towards a base case. 
# A base case is a case, where the problem can be solved without further recursion. A recursion can lead to an infinite loop, if the base case is not met in the calls.

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

def combination(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

def binomial(n, k, p):
    return combination(n,k)*(p**k)*((1-p)**(n-k))

p_family = [binomial(6, i, p_boy) for i in range(3, 7)]
# '{:06.2f}'.format() 
# For floating points the padding value represents the length of the complete output. In the example below we want our output to have at least 6 characters with 2 after the decimal point.
print("{:.3f}".format(sum(p_family)))
