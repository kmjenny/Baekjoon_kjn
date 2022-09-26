# 대표값
import sys
import statistics
nums = []
sum = 0
for i in range(10):
    a = int(sys.stdin.readline())
    sum += a
    nums.append(a)
print(sum//10)
print(statistics.mode(nums))