import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
# The string count() method returns the number of occurrences of a substring in the given string.
# The syntax of count() method is:
# string.count(substring, start=..., end=...)
def repeatedString(s, n):
    return n // len(s) * s.count('a') + s[:n % len(s)].count('a')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
