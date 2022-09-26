# 상수
import sys
a, b = map(int, sys.stdin.readline().split())

def change_num(x):
    y = 100*(x%10) + x//100
    x = x//10
    y += (x%10)*10
    return y

a = change_num(a)
b = change_num(b)

print(max(a,b))