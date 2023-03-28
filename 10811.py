# 바구니 뒤집기
# 브론즈2

import sys
N, M = map(int, sys.stdin.readline().split())
basket = [i for i in range(1,N+1)]

for x in range(M):
    i, j = map(int, sys.stdin.readline().split())
    new = basket[i-1:j]
    new.reverse()
    num = 0
    for z in range(i,j+1):
        basket[z-1] = new[num]
        num += 1

for x in basket:
    print(x, end=" ")