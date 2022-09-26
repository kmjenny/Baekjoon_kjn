# A+B - 6
import sys
T = int(sys.stdin.readline())
all = []
for i in range(T):
    A, B=map(int, sys.stdin.readline().split(','))
    all.append(A+B)
for i in all:
    print(i)