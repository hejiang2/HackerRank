numerator, denominator = map(float, input().split(' '))
first = int(input())

prob_defect = numerator / denominator

def first_detect(n, p):
    return (1 - p) ** (n - 1) * p

prob = [first_detect(i, prob_defect) for i in range(1, 6)]

print('{:.3f}'.format(sum(prob)))

# Simple solution
# 1 - P(the 1st defect is found after the first 5 inspections )
print('{:.3f}'.format(1 - (1 - prob_defect) ** first))