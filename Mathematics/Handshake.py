#!/bin/python3

import os
import sys

#
# Complete the handshake function below.
#
def handshake(n):
    #
    # Write your code here.
    #s
    s = 0
    if n == 1:
        return 0
    else: 
        while n > 0:
            s = s + (n-1)
            n -= 1
        return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = handshake(n)

        fptr.write(str(result) + '\n')

    fptr.close()
