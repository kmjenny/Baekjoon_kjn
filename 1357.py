# 뒤집힌 덧셈
import sys
X, Y = map(int, sys.stdin.readline().split())

def Rev(k):
    t = int(str(k)[::-1])
    return t

X = Rev(X)
Y = Rev(Y)
Sum = Rev(X+Y)
print(Sum)
