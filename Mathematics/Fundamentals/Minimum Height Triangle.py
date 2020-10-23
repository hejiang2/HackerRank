import sys

def lowestTriangle(base, area):
    # Complete this function
    # // operator: equivalent to division with floor a//b
    # ceil() function without math module -(-a//b)
    # 
    return -((-2*area) // base)

base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)