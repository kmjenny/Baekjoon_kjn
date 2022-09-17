# 크냐?
# 입력 여러개의 테스트 케이스 + 마지막 줄에는 0 두개

a, b=map(int, input().split())
c = list()

while a!=0 and b!=0:
    max_num = max(a,b)
    if a==b:
        c.append('No')
    elif max_num==a:
        c.append('Yes')
    else:
        c.append('No')

    a,b = map(int, input().split())

for i in c:
    print(i)