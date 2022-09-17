# 첼시를 도와줘!
n = int(input())
result = []

for i in range(n):
    p = int(input())
    all_price = 0
    all_name = ""
    for j in range(p):
        price, name = input().split()
        if int(price)>all_price:
            all_price=int(price)
            all_name=name
    result.append(all_name)

for i in result:
    print(i)