# 공 넣기
# 브론즈3

import sys
N, M = map(int, sys.stdin.readline().split())
basket = [0 for i in range(N)]

for x in range(M):
    i, j, k = map(int, sys.stdin.readline().split())

    for y in range(i-1,j):
        basket[y] = k

for z in basket:
    print(z, end=" ")