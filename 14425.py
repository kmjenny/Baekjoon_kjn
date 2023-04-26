# 문자열 집합
# 실버3
import sys
N, M = map(int, sys.stdin.readline().split())
S = set()
num = 0
for i in range(N):
    S.add(sys.stdin.readline())

for j in range(M):
    word = sys.stdin.readline()
    if word in S:
        num += 1

print(num)
