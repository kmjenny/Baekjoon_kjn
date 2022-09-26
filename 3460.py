# 이진수
import sys
all = []
T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    x = format(n, 'b')
    each = []
    for j in range(len(x)):
        if x[j]=='1':
            each.append(len(x)-j-1)
    all.append(each)

for i in range(T):
    for j in range(len(all[i])-1,-1,-1):
        if j==0:
            print(all[i][j])
        else:
            print(all[i][j], end=" ")