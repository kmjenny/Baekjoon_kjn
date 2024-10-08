# 1463
# 1로 만들기
import sys

a = int(sys.stdin.readline())
d = [0] * 1000001

for i in range(2, a+1):
    d[i] = d[i-1] + 1

    if i%2 == 0:
        d[i] = min(d[i], d[i//2] + 1)

    if i%3 == 0:
        d[i] = min(d[i], d[i//3] + 1)

print(d[a])