# 약수 구하기
import sys
N, K=map(int, sys.stdin.readline().split())
alls = []
for i in range(1,N+1):
    if N%i==0:
        alls.append(i)
if len(alls)<K:
    print("0")
else:
    print(alls[K-1])