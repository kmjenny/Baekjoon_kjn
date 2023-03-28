# 골드바흐의 추측
# 실버2

import sys
t = int(sys.stdin.readline())

def GetPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

all = list(range(2,10000))
prime = []

for i in all:
    if GetPrime(i):
        prime.append(i)

for i in range(t):
    n = int(sys.stdin.readline())
    if n%2==0:
        a = b = n//2
    else:
        a = b = int(n/2)+1

    while True:
        if a in prime and b in prime:
            print(f"{a} {b}")
            break
        else:
            a -= 1
            b += 1