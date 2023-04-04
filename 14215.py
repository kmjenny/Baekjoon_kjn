# 세 막대
# 브론즈3
import sys
import math
a, b, c = map(int, sys.stdin.readline().split())
all = []
for i in range(a,0,-1):
    for j in range(b,0,-1):
        for z in range(c,0,-1):
            s = (i + j + z) / 2
            num = s*(s-i)*(s-j)*(s-z)
            if num>0:
                S = math.sqrt(num)
                if S>0:
                    all.append(i+j+z)
print(max(all))