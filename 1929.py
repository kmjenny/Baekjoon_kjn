# 소수 구하기
# 실버3

import sys
import math
m, n = map(int, sys.stdin.readline().split())

for i in range(m,n+1):
    tmp = 0
    if i==1:
        tmp = -1
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            tmp = -1
            break
    if tmp==0:
        print(i)
