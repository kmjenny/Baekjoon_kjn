# 9461
# 파도반 수열
# 실버 3
import sys
t = int(sys.stdin.readline())

for _ in range(t):
    p = int(sys.stdin.readline())
    dp = [0] * 6
    dp[1] = dp[2] = dp[3] = 1
    dp[4] = dp[5] = 2

    if p<=5:
        print(dp[p])
    else:
        dp = dp + [0] * (p-5)
        for i in range(6, p+1):
            dp[i] = dp[i-1] + dp[i-5]
        print(dp[p])

