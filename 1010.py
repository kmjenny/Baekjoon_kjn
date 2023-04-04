# 다리 놓기
# 실버5
import sys
import math
T = int(sys.stdin.readline())
bridge = []

for i in range(T):
    n, m = map(int, sys.stdin.readline().split())
    num = math.comb(m, n)
    bridge.append(num)

for i in bridge:
    print(i)