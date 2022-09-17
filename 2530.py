# 인공지능 시계
# 입력 A(시) B(분) C(초) D(요리하는데 필요한 시간 초단위)

A, B, C = map(int, input().split())
D = int(input())

s_count = 0

# 초 계산
d = D%60
if C+d>=60:
    c=C+d-60
    s_count = 1
else:
    c=C+d

# 분 계산
if s_count==1:
    b= int(D/60)+B+1
else:
    b= int(D/60)+B

if b>=60:
    if int(b/60)>=24:
        a = A+(int(b/60)%24)
    else:
        a = A+int(b/60)
    b = b%60
else:
    a=A

if a>=24:
    a = a-24

print(f"{a} {b} {c}")