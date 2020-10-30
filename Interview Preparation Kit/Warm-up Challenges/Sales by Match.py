import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    pair = 0
    i = 0
    while i < n-1:
        if ar[i] == ar[i+1]:
            pair+=1
            i+=2
        else:
            i+=1
    return pair

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

# use dictionary

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pair = {}
    for a in ar:
        if a in pair:
            pair[a] += 1
        else:
            pair[a] = 1
    
    count = 0 
    for p in pair:
        count += (pair[p]//2)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

# use Counter
# A Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.

# cnt = Counter()
# for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
#     cnt[word] += 1
# cnt
# Output: Counter({'blue': 3, 'red': 2, 'green': 1})

from collections import Counter

n = int(input())
c = Counter(map(int, input().split()))
ans = 0

for x in c:
    ans += c[x] // 2
    
print(ans)

