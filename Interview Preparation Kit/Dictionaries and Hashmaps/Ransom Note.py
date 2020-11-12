# from collections import Counter
# Counter: a dict subclass for counting hashable objects
# It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. 
# Counts are allowed to be any integer value including zero or negative counts. 
# cnt = Counter()
# for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
      cnt[word] += 1
# cnt
# Counter({'blue': 3, 'red': 2, 'green': 1})

# c = Counter()                           # a new, empty counter
# c = Counter('gallahad')                 # a new counter from an iterable
# c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
# c = Counter(cats=4, dogs=8)             # a new counter from keyword args

# The break statement, like in C, breaks out of the innermost enclosing for or while loop.
# The continue statement, also borrowed from C, continues with the next iteration of the loop.

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine_dict = Counter(magazine)
    note_dict = Counter(note)
    replica = "Yes"
    for key, value in note_dict.items():
        if key in magazine_dict and magazine_dict[key] >= value:
            continue
        else:
            replica = "No"
            break
    print(replica)

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)


import math
import os
import random
import re
import sys
from collections import Counter
# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine_dict = Counter(magazine)
    note_dict = Counter(note)
    if note_dict - magazine_dict == {}:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

# Without Counter()
import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine_dict = {}
    replica = "Yes"
    for word in magazine:
        if word in magazine_dict.keys():
            magazine_dict[word] += 1
        else: 
            magazine_dict[word] = 1
            
    for word in note:
        if word in magazine_dict.keys() and magazine_dict[word]>0:
            magazine_dict[word] -= 1
        else: 
            replica = "No"
            break
    print(replica)
        
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

