# 가로수
# 실버4
import sys
from math import gcd
N = int(sys.stdin.readline())
wood = []

for i in range(N):
    wood.append(int(sys.stdin.readline()))

min_wood = []

for j in range(N-1,0,-1):
    min_wood.append(wood[j]-wood[j-1])

g = min_wood[0]
for j in range(1, len(min_wood)):
    g = gcd(g,min_wood[j])

result = 0
for each in min_wood:
    result += each // g-1
print(result)