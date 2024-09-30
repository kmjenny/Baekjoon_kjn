# 큐2
# 실버4
import sys
from collections import deque
N = int(sys.stdin.readline())
queue = deque()

for i in range(N):
    word = sys.stdin.readline().rstrip()
    a = len(queue)
    if 'push' in word:
        x = word[5:]
        queue.append(x)
    else:
        if word == "size":
            print(a)
        elif word == "empty":
            if a == 0:
                print("1")
            else:
                print("0")
        else:
            if a == 0:
                print("-1")
            elif word == "front":
                print(queue[0])
            elif word == "back":
                print(queue[len(queue) - 1])
            elif word == "pop":
                print(queue[0])
                queue.popleft()