import math
import os
import random
import re
import sys

from collections import Counter
# Complete the makeAnagram function below.
def makeAnagram(a, b):
    # .subtract(): Elements are subtracted from an iterable or from another mapping (or counter)
    dict_a = Counter(a)
    dict_b = Counter(b)
    dict_a.subtract(dict_b)
    return sum(abs(i) for i in dict_a.values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()




import math
import os
import random
import re
import sys

from collections import Counter
# Complete the makeAnagram function below.
def makeAnagram(a, b):
    # .elements(): Return an iterator over elements repeating each as many times as its count. 
    # Elements are returned in arbitrary order. 
    # If an element’s count is less than one, elements() will ignore it.
    res = list((Counter(b) - Counter(a)).elements()) + list((Counter(a) - Counter(b)).elements())
    return len(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
