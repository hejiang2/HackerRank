import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    luck_max = sum([contests[i][0] for i in range(len(contests))])
    important = []
    for i in range(len(contests)):
        if contests[i][1] == 1:
            important.append(contests[i][0])
    important.sort()
    win = sum([important[i] for i in range(len(important)-k)])
    return luck_max - win*2

# Complete the luckBalance function below.
def luckBalance(k, contests):
    luck = 0
    for lck, imp in sorted(contests, reverse=True):
        if k > 0 or not imp:
            luck += lck
            k -= imp
        else:
            luck -= lck
    return luck


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
