# 피보나치 수 2
import sys
n = int(sys.stdin.readline())
a = 0
b = 1
count = 0
for i in range(2,n+1):
    if count==0:
        a=a+b
        count=1
    else:
        b=a+b
        count=0
if count==0:
    print(b)
else:
    print(a)