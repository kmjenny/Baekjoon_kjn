# 다면체
import sys
T = int(sys.stdin.readline())
result = []
for i in range(T):
    V, E = map(int, sys.stdin.readline().split())
    result.append(2-V+E)
for i in result:
    print(i)