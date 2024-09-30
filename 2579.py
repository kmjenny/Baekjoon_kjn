# 2579
# 계단 오르기
# 실버 3
import sys
n = int(sys.stdin.readline())
stair = [0] * 301

for i in range(1, n+1):
    stair[i] = int(sys.stdin.readline())

dp = [0] * 301
dp[1] = stair[1]
dp[2] = stair[1] + stair[2]
dp[3] = max(stair[1] + stair[3], stair[2] + stair[3])

for i in range(4, n+1):
    dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])

print(dp[n])
