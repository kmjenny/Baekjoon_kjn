# 최소공배수
# 실버5
import sys
A,B = map(int, sys.stdin.readline().split())

def GCD(x,y):
    while(y):
        x,y=y,x%y
    return x
def LCM(x,y):
    result = (x*y)//GCD(x,y)
    return result

print(LCM(A,B))