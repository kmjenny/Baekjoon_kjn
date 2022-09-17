# 전자레인지
# 버튼 A(5분=300초), B(1분=60초), C(10초)

T = int(input())
a=0
b=0
c=0

if T%10!=0:
    print("-1")
else:
    a=T//300
    b=(T%300)//60
    c=(T%300)%60//10
    print(a, b, c)

