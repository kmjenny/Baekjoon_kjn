# 설탕 배달
# 실버4

import sys
n = int(sys.stdin.readline())
# 봉지는 3킬로그램, 5킬로그램
# 1. 5킬로그램만으로 가능(무조건 최소)
# 2. 3킬로그램만으로 가능
# 3. 섞어서(5킬로짜리 먼저 / 3킬로짜리 먼저 / 적당하게)

if n%5==0: # 1번
    print(n//5)
else:
    p = 0
    while n>0:
        n -= 3
        p += 1
        if n%5==0: # 3번
            p += n//5
            print(p)
            break
        elif n == 1 or n == 2: # 불가능
            print(-1)
            break
        elif n == 0: # 2번
            print(p)
            break