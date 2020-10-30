# Array: a container object that holds a fixed number of values that have a single datatype

# Python arrays are a data structure like lists. 
# They contain a number of objects that can be of different data types.
# In addition, Python arrays can be iterated and have a number of built-in functions to handle them.
# Arrays are useful if you want to work with many values of the same Python data type.
# They make it easy to perform the same operation on multiple values at the same time.
# Each value in an array has an index number, which tells us where the item is within an array. Indexes start with and correspond with a certain item in an array.
# Python Array Methods
# Using the append() array operation allows us to add an element to the end of our array, without declaring a new array.
# Python pop() works in the same way as append(), but it works as a remove method that deletes an item from an array. In addition, pop() takes an index number as an argument, rather than a string.
# clear(): removes all items from an array
# copy(): returns a copy of an array
# count(): returns the number of elements in a list
# index(): returns the index of the first element with a specific value
# insert(): adds an element to the array at the specific position
# reverse(): reverses the order of the array
# sort(): sort the list

# Unpacking argument lists: occurs when the arguments are already in a list or tuple but need to be unpacked for a function call requiring separate positional arguments.
# For instance, the built-in range() function expects separate start and stop arguments. If they are not available separately, write the function call with the *-operator to unpack the arguments out of a list or tuple:
# args = [3, 6]
# list(range(*args)) 

# Method 1: Using the slicing technique
# In this technique, a copy of the list is made and the list is not sorted in-place. Creating a copy requires more space to hold all of the existing elements. This exhausts more memory.
# [start : stop : steps] which means that slicing will start from index start will go up to stop in step of steps. Default value of start is 0, stop is last index of list and for step it is 1.
# [: stop] will slice list from starting till stop index and [start : ] will slice list from start index till end.
# Negative value of steps shows right to left traversal instead of left to right traversal that is why [: : -1] prints list in reverse order.
# * removes [] and ','.

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    print(*arr[::-1])

# Method 2: Using the reversed() built-in function.
# In this method, we neither reverse a list in-place(modify the original list), nor we create any copy of the list. Instead, we get a reverse iterator which we use to cycle through the list.

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    print(*reversed(arr))

# Method 3: Using the reverse() built-in function.
# Using the reverse() method we can reverse the contents of the list object in-place i.e., we don’t need to create a new list instead we just copy the existing elements to the original list in reverse order. This method directly modifies the original list.

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    arr.reverse()
    print(*arr)

