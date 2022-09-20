# 별 찍기-16
import sys
N = int(sys.stdin.readline())
for i in range(1,N+1):
    print("{0}{1}".format(" "*(N-i),"*"), end="")
    for j in range(i-1):
        print(" *", end="")
    print()