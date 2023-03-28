# 행렬 덧셈
# 브론즈5

import sys
n, m = map(int, sys.stdin.readline().split())

A = []
B = []
for i in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    A.append(arr)

for i in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    B.append(arr)

for i in range(n):
    for j in range(m):
        print(A[i][j]+B[i][j], end=" ")
    print()