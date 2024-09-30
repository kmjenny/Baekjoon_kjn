# 스택 수열
# 실버2
import sys
from collections import deque

n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    stack.append(int(sys.stdin.readline()))

stack = deque(stack)
nums = []
result = []

i = 0
check = 0
while stack:
    if len(nums) == 0:
        i += 1
        nums.append(i)
        result.append("+")

    if nums[-1] == stack[0]:
        result.append("-")
        stack.popleft()
        nums.pop()
    elif nums[-1] > stack[0]:
        check = 1
        break
    else:
        i += 1
        nums.append(i)
        result.append("+")

if check == 1:
    print("NO")
else:
    for i in result:
        print(i)