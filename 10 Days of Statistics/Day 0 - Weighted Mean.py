#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 17:09:01 2020

@author: fiona
"""

n = int(input())
nums = [int(i) for i in input().split(' ')]
weights = [int(i) for i in input().split(' ')]
nums_weights = [nums[i] * weights[i] for i in range(n)]
weight_mean = sum(nums_weights) / sum(weights)
print("{:.1f}".format(weight_mean))
