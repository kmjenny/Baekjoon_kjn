# 붙임성 좋은 총총이
# 실버4
import sys
N = int(sys.stdin.readline())
people = set()
people.add("ChongChong")

for i in range(N):
    A, B = sys.stdin.readline().split()
    if A in people and B in people:
        continue
    elif A in people and B not in people:
        people.add(B)
    elif A not in people and B in people:
        people.add(A)

print(len(people))
