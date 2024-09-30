# 1158
# 요세푸스 문제
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
nums = deque()
nums = deque(range(1,n+1))

print("<", end="")
while len(nums)!=0:
    for i in range(1, k+1):
        if i%k == 0:
            x = nums.popleft()
            print(x, end="")
            if len(nums)!= 0:
                print(", ", end="")
            else:
                print(">")
        else:
                nums.append(nums.popleft())