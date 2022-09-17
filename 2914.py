# 저작권
# 입력 A(앨범에 수록된 곡의 개수), I(평균값)

A, I = map(int, input().split())

all = A*I
for i in range(all+1):
    if I-1<i/A<=I:
        print(i)
        break