# 알고리즘 수업 - 점근적 표기 1
# 실버4
import sys
one, two = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
n = int(sys.stdin.readline())

fn = one*n + two
g = c*n

if fn<=g and c>=one:
    print("1")
else:
    print("0")