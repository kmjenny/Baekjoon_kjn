# 좌표 압축
# 실버2
import sys
N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))
x_set = set(X)
x = list(x_set)
x.sort()

num = {}
for i in range(len(x)):
    num[x[i]] = i

for i in X:
    print(num[i], end=' ')