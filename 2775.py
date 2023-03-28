# 부녀회장이 될테야
# 브론즈1

import sys
t = int(sys.stdin.readline())
num = []

for i in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    f0 = [x for x in range(1,n+1)] # 0층 리스트
    for p in range(k):
        for j in range(1, n):
            f0[j] += f0[j-1]
    num.append(f0[-1])

for i in num:
    print(i)