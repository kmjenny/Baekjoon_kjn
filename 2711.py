# 오타맨 고창영
import sys
T = int(sys.stdin.readline())
all = []
for i in range(T):
    a, b = sys.stdin.readline().split()
    a = int(a)
    b = b[:a-1] + b[a:]
    all.append(b)
for i in all:
    print(i)