# 1904
# 01타일
# 실버 3
import sys

n = int(sys.stdin.readline())
num = 15746
dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
    dp[i] = (dp[i-1] + dp[i-2])%num

print(dp[n])