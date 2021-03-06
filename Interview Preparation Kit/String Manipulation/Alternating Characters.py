import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    deletions = {'Black':0, 'Red':0}
    for i in range(len(s)-1):
        if s[i+1] != s[i]:
            deletions['Black'] += 1
        else:
            deletions['Red'] += 1
    return deletions['Red']

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')


import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    deletions = 0
    for i in range(len(s)-1):
        if s[i+1] == s[i]:
            deletions += 1
    return deletions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
