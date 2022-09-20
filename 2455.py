# 지능형 기차
import sys
peoples = []
people = 0
for i in range(4):
    a, b=map(int,sys.stdin.readline().split())
    people = people-a+b
    peoples.append(people)
print(max(peoples))