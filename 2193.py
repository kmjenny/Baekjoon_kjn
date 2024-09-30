# 2193
# 이친수
# 실버 3
import sys

# n은 자릿수
n = int(sys.stdin.readline())
# 0으로 시작하지 않는다
# 1이 두 번 연속 나타나지 않는다

dp = [0] * (n+1)
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n])