import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    hiking = {'mountain': 0, 'valley': 0}
    l = 0
    for i in path:
        if i == 'U':
            l += 1
            if l == 0:
                hiking['valley'] += 1
        else:
            l -= 1
            if l == 0:
                hiking['mountain'] +=1
    return hiking['valley']

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

# Slightly more compactly:
def countingValleys(n, s):
    level = valleys = 0
    for step in s:
        level += 1 if step == "U" else -1
        valleys += level == 0 and step == "U"
    return valleys