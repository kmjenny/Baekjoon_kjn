# A+B-3
T = int(input())
result = []
for i in range(T):
    a,b = map(int, input().split())
    result.append(a+b)

for i in result:
    print(i)