# 2493
# 탑
import sys

N = int(sys.stdin.readline())
h = list(map(int, sys.stdin.readline().split()))
stack = []
ans = [0 for i in range(N)]

for i in range(N):
    while stack:
        if stack[-1][1] > h[i]:
            ans[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, h[i]])

print(*ans)