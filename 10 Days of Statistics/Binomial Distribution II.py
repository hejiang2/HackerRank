# Enter your code here. Read input from STDIN. Print output to STDOUT
reject, batch = map(int, input().split(' '))

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

def nCr(n, r):
    return factorial(n) / (factorial(r) * factorial(n-r))

def binomial(n, r, p):
    return nCr(n, r) * (p**(r)) * ((1 - p)**(n - r))

def no_more_than(n, k, p):
    prob = [binomial(n, i, p) for i in range(k+1)]
    return sum(prob)

def at_least(n, k, p):
    prob = [binomial(n, i, p) for i in range(k, n+1)]
    return sum(prob)

print('{:.3f}'.format(no_more_than(batch, 2, reject/100.0)))
print('{:.3f}'.format(at_least(batch, 2, reject/100.0)))
