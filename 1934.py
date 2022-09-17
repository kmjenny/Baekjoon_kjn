# 최소공배수
# 입력 T(테스트의 개수), A와 B T번 주어짐

T = int(input())
C = list()

for i in range(T):
    a, b = map(int,input().split())
    x, y = max(a,b),min(a,b)
    while y:
        x,y=y,x%y # 최대공약수 구한 후에 두 수의 곱을 최대공약수로 나누기
    C.append(a*b//x)

for i in range(T):
    print(C[i])