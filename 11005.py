# 진법 변환 2
# 브론즈1
import sys
N, B = map(int, sys.stdin.readline().split())

if B==10:
    print(N)
elif B<10:
    num = []
    while True:
        n = N%B
        N = N//B
        num.append(n)
        if N == 0:
            break
    num.reverse()
    for i in num:
        print(i, end="")
elif B>10:
    num = []
    while True:
        n = N%B
        N = N//B
        if n>=10:
            x = chr(n+55)
            num.append(x)
        else:
            num.append(n)
        if N == 0:
            break
    num.reverse()
    for i in num:
        print(i, end="")