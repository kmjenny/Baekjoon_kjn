# 11726
# 2xn 타일링
# 실버3
import sys
n = int(sys.stdin.readline())
num = 10007
dp = [0] * 1001
dp[1] = 1
dp[2] = 2

if n<=2:
    print(dp[n]%10007)
else:
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n]%10007)
