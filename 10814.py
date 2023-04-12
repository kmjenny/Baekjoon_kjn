# 나이순 정렬
# 실버5
import sys
N = int(sys.stdin.readline())
member = []

for _ in range(N):
    age, name = sys.stdin.readline().split()
    age = int(age)
    member.append((age, name))

result = sorted(member, key = lambda x : x[0])

for i in result:
    for j in i:
        print(j, end=" ")
    print()