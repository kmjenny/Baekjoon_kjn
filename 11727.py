# 11727
# 2xn 타일링 2
# 실버 3
import sys
n = int(sys.stdin.readline())
num = 10007
dp = [0] * (n+1)

dp[1] = 1

if n > 1:
    dp[2] = 3
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + 2*dp[i-2])%num

print(dp[n])