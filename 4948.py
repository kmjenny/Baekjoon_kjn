# 베르트랑 공준
# 실버2

import sys

def GetPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

all = list(range(2,246912))
prime = []

for i in all:
    if GetPrime(i):
        prime.append(i)

while True:
    n = int(sys.stdin.readline())
    if n==0:
        break
    count = 0

    for i in prime:
        if n<i<=2*n:
            count += 1
    print(count)