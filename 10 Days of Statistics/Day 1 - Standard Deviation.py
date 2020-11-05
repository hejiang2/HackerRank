n = int(input())
nums = [int(i) for i in input().split(' ')]

mu = sum(nums)/n
dev = [(nums[i]-mu)**2 for i in range(n)]
# 1/2 is doing integer division: 1/2 == 0
sd = (sum(dev)/n)**(1.0/2)
print("{:.1f}".format(sd))