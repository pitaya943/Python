# coding=utf-8
import sys
# if input = [2, 3, 5, 7, 8] and target = 5
# Output should be [0, 1] because input[0] + input[1] = 5 (target)

nums = []

for i in range(0, 5):
    num = int(input("input array[]: "))
    nums.append(num)
target = int(input("targer num :"))

seen = {}
output = []
for i, v in enumerate(nums):
    remaining = target - v
    if remaining in seen:
        output = [seen[remaining], i]
        print(output)
    seen[v] = i
