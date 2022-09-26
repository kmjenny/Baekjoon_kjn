# 숫자의 합
import sys
N = int(sys.stdin.readline())
nums = sys.stdin.readline()
sum = 0
for i in range(N):
    sum += int(nums[i])
print(sum)