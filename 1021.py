# 1021
# 회전하는 큐
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
x = deque(i for i in range(1,N+1))
result = 0

for i in num:
    if x.index(i)>(N//2):
        while i!=x[0]:
            x.rotate(1)
            result += 1
    else:
        while i!=x[0]:
            x.rotate(-1)
            result += 1
    x.popleft()
    N -= 1
    

print(result)
