# 개수 세기
import sys
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())
count = 0
for i in nums:
    if v==i:
        count += 1
print(count)