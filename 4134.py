# 다음 소수
# 실버4
import sys
from math import sqrt
n = int(sys.stdin.readline())

def isPrime(x):
    if x == 1 or x == 0:
        return False
    for i in range(2, int(sqrt(x))+1):
        if x%i==0:
            return False
    return True

for i in range(n):
    check = 0
    num = int(sys.stdin.readline())
    while True:
        if isPrime(num) == True:
            print(num)
            break
        else:
            num += 1

