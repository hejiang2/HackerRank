numerator, denominator = map(float, input().split(' '))
first = int(input())

prob_defect = numerator / denominator
prob = (1 - prob_defect) ** (first - 1) * prob_defect
print('{:.3f}'.format(prob))