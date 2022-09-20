# 더하기
import sys
T = int(sys.stdin.readline())
nums = []
for i in range(T):
    N = int(sys.stdin.readline())
    sum = 0
    num = list(map(int,sys.stdin.readline().split()))
    for j in range(N):
        sum += num[j]
    nums.append(sum)
for i in nums:
    print(i)