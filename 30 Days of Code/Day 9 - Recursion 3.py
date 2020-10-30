# What is recursion?
# The process of defining a function or calculating a number by the repeated application of an algorithm.
# russian dolls, mirrors
# recursion consists of:
# 1. base case: when we stop repeating our algorithm
# 2. recursive case: repeating the algorithm

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
