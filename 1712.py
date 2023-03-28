# 손익분기점
# 브론즈2

import sys

A, B, C = map(int, sys.stdin.readline().split())

if B>=C:
    print(-1)
else:
    num = A/(C-B)+1
    print(int(num))