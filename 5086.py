# 배수와 약수
# factor(첫번째 수가 두번째 수의 약수)
# multiple(첫번째 수가 두번째 수의 배수)
# neither(둘다 아님)

a, b=map(int, input().split())
result = []

while a!=0 and b!=0:
    if b%a==0:
        result.append('factor')
    elif a%b==0:
        result.append('multiple')
    else:
        result.append('neither')

    a,b=map(int,input().split())

for i in result:
    print(i)