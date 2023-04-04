# 중앙 이동 알고리즘
# 브론즈3
import sys

N = int(sys.stdin.readline())
arr = [0 for i in range(16)]

point = 2
d = 1
arr[0] = 4
for i in range(1,16):
    point += d
    arr[i] = pow(point, 2)
    d *= 2
print(arr[N])
