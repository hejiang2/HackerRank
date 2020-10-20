#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 15:13:44 2020

@author: fiona
"""

# input() function
# x = input("Enter your name:")
# print("Hello, " + x)

# Day 0: Mean, Median, and Mode
n =  int(input()) # change a string to an integer
nums = [int(i) for i in input().split(' ')]
# Mean
mean = sum(nums)/n

# Median
nums.sort()
if n % 2 == 1:
    median = nums[(n - 1) / 2]
else:
    median = (nums[int(n / 2)] + nums[int(n / 2 - 1)]) / 2

# Mode
# The count() method returns the number of elements with the specified value.
max_nums = max([nums.count(i) for i in set(nums)])
for i in nums:
    if nums.count(i) == max_nums:
        mode = i
        break
print(mean)
print(median)
print(mode)
    
