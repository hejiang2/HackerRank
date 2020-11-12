import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
# Printing and returning are completely different concepts.
# print is a function you call. 
# Calling print will immediately make your program write out text for you to see. 
# Use print when you want to show a value to a human.
# return is a keyword. 
# When a return statement is reached, Python will stop the execution of the current function, sending a value out to where the function was called. 
# Using return changes the flow of the program. Using print does not.
def minimumBribes(q):
    bribe = 0
    for i in range(len(q)-1, -1, -1):
        if q[i]!=i+1:
            if q[i-1] == i+1:
                bribe += 1
                q[i-1], q[i] = q[i], q[i-1]
            elif q[i-2] == i+1:
                bribe += 2
                q[i-2], q[i-1] = q[i-1], q[i-2]
                q[i-1], q[i] = q[i], q[i-1]
            else:
                print("Too chaotic")
                return
    print(bribe)

# Simply count how many times has a person been bribed by looking at who is ahead of this person.
def minimumBribes(q):
    bribe = 0
    for i in range(len(q)):
        if q[i] - (i+1) > 2:
            print("Too chaotic")
            return
        for j in range(max(0, q[i]-2) , i):
            if q[j]>q[i]:
                bribe += 1
    print(bribe)

            
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
