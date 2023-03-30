# 색종이
# 실버5

import sys
N = int(sys.stdin.readline())
maximum = [[0 for i in range(100)] for j in range(100)]

for k in range(N):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(10):
        for j in range(10):
            maximum[x+i][y+j] = 1

check = 0
for i in maximum:
    for j in i:
        if j==1:
            check += 1

print(check)
