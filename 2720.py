# 세탁소 사장 동혁
# 브론즈3

# 쿼터 0.25
# 다임 0.10
# 니켈 0.05
# 페니 0.01

import sys

T = int(sys.stdin.readline())
money = [25, 10, 5, 1]
Q = []
D = []
N = []
P = []

for i in range(T):
    c = int(sys.stdin.readline())
    q = 0
    d = 0
    n = 0
    p = 0
    for j in money:
        if c==0:
            break
        if c>=j:
            if j==25:
                q += c//j
                c -= c//j*j
            elif j==10:
                d += c//j
                c -= c//j*j
            elif j==5:
                n += c//j
                c -= c//j*j
            elif j==1:
                p += c//j
                c -= c//j*j
    Q.append(q)
    D.append(d)
    N.append(n)
    P.append(p)

for i in range(T):
    print(f"{Q[i]} {D[i]} {N[i]} {P[i]}")

