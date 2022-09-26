# 대표값2
import sys
nums = []
for i in range(5):
    num = int(sys.stdin.readline())
    nums.append(num)
nums.sort()
print(sum(nums)//5)
print(nums[2])
