# 과자
# 입력 K(과자 한 개의 가격), N(사려고 하는 과자의 개수), M(동수가 가진 돈)

K, N, M = map(int, input().split())

if K*N>M:
    pin_money = (M-K*N)*-1
else:
    pin_money = 0

print(pin_money)