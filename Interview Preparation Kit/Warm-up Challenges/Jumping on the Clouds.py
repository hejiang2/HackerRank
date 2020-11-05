import math
import os
import random
import re
import sys

# Method 1: regular 
import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
# 010, 001, 000
# 011 then we could void the path entirely as she can jump to i+2 maximum
def jumpingOnClouds(c):
    jumps = position = 0
    # len(c)-1: not the last cloud
    while position < len(c)-1:
        if position + 2 < len(c) and c[position+2] == 0:
            position += 2
            jumps += 1
        elif c[position+1] == 0: 
            position += 1
            jumps += 1
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

# # Method 2: no position needed 
import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    c = [str(s) for s in c]
    # The join() method takes all items in an iterable and joins them into one string.
    c = ''.join(c)
    jump = c.count('1')
    # The split() method splits a string into a list. 
    # You can specify the separator, default separator is any whitespace.
    c = c.split('1')
    for seg in c:
        jump+=len(seg)//2
    return jump


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
