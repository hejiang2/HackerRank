n = int(input())
nums = [int(i) for i in input().split(' ')]
freq = [int(i) for i in input().split(' ')]
list = []
# We should create a list with the iter that we want to create and use the * operator to get the repeat list as follows.
# ['a'] * 10
for i in range(n):
    list.extend([nums[i]] * freq[i])
list.sort()

def median(n, nums):
    if n%2 == 0:
        median = 0.5 * nums[n//2] + 0.5 * nums[n//2 - 1]
    else:
        median = nums[n//2]
    return median

if len(list) % 2 == 0:
    q1 = median(len(list[:len(list)//2]), list[:len(list)//2])
    q3 = median(len(list[len(list)//2:]), list[len(list)//2:])
else: 
    q1 = median(len(list[:len(list)//2]), list[:len(list)//2])
    q3 = median(len(list[len(list)//2+1: ]), list[len(list)//2+1:])

print("{:.1f}".format(q3-q1))
