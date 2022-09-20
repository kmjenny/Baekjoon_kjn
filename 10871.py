# X보다 작은 수
import sys
N, X = map(int, sys.stdin.readline().split())
B = []
A = list(map(int, sys.stdin.readline().split()))

for i in A:
    if i<X:
        B.append(i)

for i in B:
    print(i, end=" ")
