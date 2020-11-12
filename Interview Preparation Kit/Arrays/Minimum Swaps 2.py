# The trick is to put every element in the place it belongs to and swap it with the element at that position. 
# It is possible that the swapped element wont be the correct once, hence the while loop.
# 1 3 5 2 4 6 7
# 1 5 3 2 4 6 7
# 1 4 3 2 5 6 7
# 1 2 3 4 5 6 7

# a,b = b,a
# In fact, what Python does is first it "prepares" the values of the right side by creating a tuple (b,a). Then this tuple is unpacked and assigned to the variables in the reverse order. (a first)


# a = [2,1,0]
# a[0], a[a[0]] = a[a[0]], a[0]
# 1. a[a[0]] takes the value from the a[0] element (equal to 2) of the list a (value 0).
# 2. a[0] is 2 hence the tuple created is (0,2).
# 3. Tuple (0,2) is unpacked and 0 replaces 2 in the list (a[0]).
# 4. Now, a[a[0]] can be read as: take 0th element of list a (which is 0) and then replace the value in the list at that place with 2 from tuple unpacking (now 0 is replaced by 2).
# DO NOT USE arr[i], arr[arr[i]-1] = arr[arr[i]-1], arr[i]

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    for i in range(len(arr)):
        while arr[i] != i+1:
            temp = arr[i]-1
            arr[i], arr[temp] = arr[temp], arr[i]
            swaps += 1
    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
