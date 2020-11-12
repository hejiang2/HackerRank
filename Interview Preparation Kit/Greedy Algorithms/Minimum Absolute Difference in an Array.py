# Greedy Algorithms
# A greedy algorithm is a simple, intuitive algorithm that is used in optimization problems. 
# The algorithm makes the optimal choice at each step as it attempts to find the overall optimal way to solve the entire problem. 

# The most direct solution would be to calculate the absolute difference between each element with the elements after it. The time complexity will be O(n^2).
# If we sort the list first, then we can only compare the neighbors. The new time complexity will be O(nlogn).

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort()
    min_diff = arr[1] - arr[0]
    for i in range(2, len(arr)):
        if arr[i] - arr[i-1] < min_diff:
            min_diff = arr[i] - arr[i-1]
    return min_diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort()
    return min(y-x for x, y in zip(arr, arr[1:]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

