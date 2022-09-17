# 오븐시계
# 입력 A(시), B(분), C(요리하는데 필요한 시간)

def oven_timer(a, b, c):
    check = 0
    if b+c>=60:
        check = (b + c) // 60
        b = (b+c)%60
    else:
        b = b+c

    if check!=0:
        a = a+check
        if a>=24:
            a = a-24

    print(f"{a} {b}")

A, B = map(int,input().split())
C = int(input())

oven_timer(A,B,C)
