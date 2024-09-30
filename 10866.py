# 10866
# 덱
import sys
from collections import deque

N = int(sys.stdin.readline())
num = deque()

for _ in range(N):
    x = list(sys.stdin.readline().split())

    if x[0]=='push_front':
        num.appendleft(x[1])
    elif x[0]=='push_back':
        num.append(x[1])
    elif x[0]=='pop_front':
        if len(num)==0:
            print("-1")
        else:
            print(num.popleft())
    elif x[0]=='pop_back':
        if len(num)==0:
            print("-1")
        else:
            print(num.pop())
    elif x[0]=='size':
        print(len(num))
    elif x[0]=='empty':
        if len(num)==0:
            print("1")
        else:
            print("0")
    elif x[0]=='front':
        if len(num)==0:
            print("-1")
        else:
            print(num[0])
    elif x[0]=='back':
        if len(num)==0:
            print("-1")
        else:
            print(num[-1])