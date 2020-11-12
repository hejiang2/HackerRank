# Brute-force search (exhaustive search)
# The aim: we would like to construct an algorithm thats capable of finding a pattern in a text.
# Brute-force search is the naive approach.

# Anagram:
# 1. len(s1) = len(s2)
# 2. freq of each char in s1 = freq of each char in s2

# a HashMap like [{a:3}, {aa:2}]
# number of pairs = n(n-1)/2

# Program to print all substrings of a given string.
# The outer loop picks lengths of strings for a given starting point.
# The inner loop picks starting character.
# The sorted() function returns a sorted list of the specified iterable object.
# s = 'happy'
# for i in range(1, len(s)):
#   for j in range(len(s)-i+1):
#     print(s[j:j+i])
#     print(str(sorted(s[j:j+i]))) 
# h
# ['h']
# a
# ['a']
# p
# ['p']
# p
# ['p']
# y
# ['y']
# ha
# ['a', 'h']
# ap
# ['a', 'p']
# pp
# ['p', 'p']
# py
# ['p', 'y']
# hap
# ['a', 'h', 'p']
# app
# ['a', 'p', 'p']
# ppy
# ['p', 'p', 'y']
# happ
# ['a', 'h', 'p', 'p']
appy
['a', 'p', 'p', 'y']

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    substrings = {}
    anagram = 0
    for i in range(1, len(s)):
        for j in range(len(s)-i+1):
            substr = str(sorted(s[j:j+i])) # list is unhashable
            if substr in substrings.keys():
                substrings[substr] += 1
            else:
                substrings[substr] = 1
    for val in substrings.values():
        anagram += val*(val-1)/2
    return int(anagram)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

    
# The join() method takes all items in an iterable and joins them into one string.
# The get() method returns the value of the item with the specified key.
# Syntax: dictionary.get(keyname, value)
# keyname: Required. The keyname of the item you want to return the value from
# value: Optional. A value to return if the specified key does not exist. 

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    substrings = {}
    anagram = 0
    for i in range(1, len(s)):
        for j in range(len(s)-i+1):
            substr = ''.join(sorted(s[j:j+i]))
            substrings[substr] = substrings.get(substr,0) + 1
    for val in substrings.values():
        anagram += val*(val-1)//2
    return anagram

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
