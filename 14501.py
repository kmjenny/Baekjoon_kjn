# 14501
# 퇴사
# 실버 3
import sys
n = int(sys.stdin.readline())
dp = [0] * (n+1)
tp = [list(map(int, input().split())) for _ in range(n)]

for i in range(n-1, -1, -1):
    if tp[i][0] > n-i:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i+tp[i][0]]+tp[i][1])

print(dp[0])