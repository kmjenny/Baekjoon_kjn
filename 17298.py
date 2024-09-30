# 17298
# 오큰수
import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
num = []
result = [-1 for _ in range(N)]
count = 0

for i in range(N):
    while num and A[num[-1]] < A[i]:
        result[num.pop()] = A[i]
    num.append(i)

for i in result:
    print(i, end=" ")
