# 달팽이는 올라가고 싶다
# 브론즈1

import sys
import math
a, b, v = map(int, sys.stdin.readline().split())

count = math.ceil((v-a)/(a-b))

print(int(count)+1)