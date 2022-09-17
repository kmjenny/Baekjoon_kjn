# 소인수분해
# 입력 N(1<=N<=10,000,000)

N = int(input())

while(N!=1):
    for i in range(2, N+1):
        if N%i==0:
            print(i)
            N = int(N/i)
            break