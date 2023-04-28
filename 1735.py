# 분수 합
# 실버3
import sys
a,b = map(int, sys.stdin.readline().split())
c,d = map(int, sys.stdin.readline().split())

y = b*d
x = a*d+c*b

def GCD(x,y):
    while(y):
        x,y = y,x%y
    return x

while True:
    num = GCD(x,y)
    if num!=1:
        x = x//num
        y = y//num
    elif num==1:
        break

print(f"{x} {y}")