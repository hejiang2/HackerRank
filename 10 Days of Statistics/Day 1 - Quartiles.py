#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 10:58:08 2020

@author: fiona
"""

# // returns the integral part of the quotient.
n = int(input())
nums = [int(i) for i in input().split(' ')]
nums.sort()
def median(n, nums):
    if n % 2 == 0:
        median = 0.5 * nums[n//2] + 0.5 * nums[n//2-1]
    else:
        median = nums[n//2]
    return median

q2 = median(n, nums)
if n % 2 == 0:
    q1 = median(len(nums[:n//2]), nums[:n//2])
    q3 = median(len(nums[n//2:]), nums[n//2:])
else: 
    q1 = median(len(nums[:n//2]), nums[:n//2])
    q3 = median(len(nums[n//2+1:]), nums[n//2+1:])


print(int(q1))
print(int(q2))
print(int(q3))