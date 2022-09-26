# 주차의 신
import sys
T = int(sys.stdin.readline())
all = []
for i in range(T):
    shop = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    all.append((max(nums)-min(nums))*2)

for i in all:
    print(i)