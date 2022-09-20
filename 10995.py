# 별 찍기-20
import sys
N = int(sys.stdin.readline())
for i in range(1,N+1):
    if i%2==1:
        for j in range(1,2*N):
            if j%2==1:
                print("*", end='')
            else:
                print(" ", end='')
        print()
    else:
        for j in range(1,2*N+1):
            if j%2==1:
                print(" ", end='')
            else:
                print("*", end='')
        print()