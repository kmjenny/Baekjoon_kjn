# 지능형 기차2
import sys
all = []
people = 0
for i in range(10):
    a, b = map(int, sys.stdin.readline().split())
    people = people-a+b
    all.append(people)
print(max(all))