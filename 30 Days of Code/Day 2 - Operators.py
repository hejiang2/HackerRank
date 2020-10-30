# int / int = int
# As a % is a fraction < 1, the result evaluates to 0 in integer division.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * (tip_percent/100.0)
    tax = meal_cost * (tax_percent/100.0)
    total_cost = round(meal_cost + tip + tax)
# The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.
# The default number of decimals is 0, meaning that the function will return the nearest integer.
    print(total_cost)
# return != print


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
