# 바구니 순서 바꾸기
# 브론즈2

import sys
N, M = map(int, sys.stdin.readline().split())
basket = [i for i in range(1,N+1)]

# i j k
# begin end mid
# mid ~ end begin ~ mid-1
# k ~ j i ~ j-1
for x in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    new = basket[k-1:j]
    for y in range(i-1,k-1):
        new.append(basket[y])
    num=0
    for y in range(i-1,j):
        basket[y] = new[num]
        num+=1

for x in basket:
    print(x, end=" ")