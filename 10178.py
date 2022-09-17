# 할로윈의 사탕
import sys
T = int(sys.stdin.readline())
child = []
dad = []
for i in range(T):
    c,v =map(int,sys.stdin.readline().split())
    child.append(int(c/v))
    dad.append(c%v)
for i in range(T):
    print(f"You get {child[i]} piece(s) and your dad gets {dad[i]} piece(s).")