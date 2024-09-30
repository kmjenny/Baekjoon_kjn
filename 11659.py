# 11659
# 구간 합 구하기 4
# 실버3
import sys
n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
np = [0] * 100001
np[1] = num[0]

for i in range(2, n+1):
    np[i] = np[i-1] + num[i-1]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    result = np[j] - np[i-1]
    print(result)