# 11328
# Strfry
import sys

N = int(sys.stdin.readline())

for i in range(N):
    a, b = sys.stdin.readline().split()
    x = ''.join(sorted(a))
    y = ''.join(sorted(b))
    if x == y:
        print("Possible")
    else:
        print("Impossible")

