# 플러그
import sys
N = int(sys.stdin.readline())
result = 0
for i in range(N):
    t = int(sys.stdin.readline())
    result += t
print(result-N+1)