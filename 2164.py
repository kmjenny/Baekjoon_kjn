# 카드2
# 실버4
import sys
from collections import deque
n = int(sys.stdin.readline())
queue = deque()

for i in range(2,n+1):
    queue.append(i)

if n<3:
    print(n)
else:
    for i in range(n-2):
        queue.append(queue.popleft())
        queue.popleft()

    print(queue.popleft())