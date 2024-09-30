# 6198
# 옥상 정원 꾸미기
import sys

N = int(sys.stdin.readline())
h = []
for _ in range(N):
    h.append(int(sys.stdin.readline()))
stack = []
ans = 0

for i in range(N):
    while(len(stack)!=0 and stack[-1] <= h[i]):
        stack.pop()
        ans += len(stack)
    stack.append(h[i])

while(len(stack)!=0):
    stack.pop()
    ans += len(stack)

print(ans)