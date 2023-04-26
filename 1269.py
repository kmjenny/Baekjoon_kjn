# 대칭 차집합
# 실버4
import sys
a, b = map(int, sys.stdin.readline().split())
A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))

C = set.symmetric_difference(A,B)
print(len(C))