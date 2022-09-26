# 사과
import sys
N = int(sys.stdin.readline())
all = 0
for i in range(N):
    s, a = map(int, sys.stdin.readline().split())
    all = all + (a%s)
print(all)