# 듣보잡
# 실버4
import sys
N, M = map(int, sys.stdin.readline().split())
a = set()
b = set()

for i in range(N):
    word = sys.stdin.readline().rstrip()
    a.add(word)
for j in range(M):
    word = sys.stdin.readline().rstrip()
    b.add(word)

c = set.intersection(a,b)
c = sorted(c)

print(len(c))
for i in c:
    print(i)