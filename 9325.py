# 얼마?
T = int(input())
result = []
for i in range(T):
    s = int(input())
    price = s
    n = int(input())
    for j in range(n):
        q, p=map(int, input().split())
        price+=q*p
    result.append(price)
for i in result:
    print(i)

