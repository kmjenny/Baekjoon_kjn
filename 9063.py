# 대지
# 브론즈3
import sys
N = int(sys.stdin.readline())
A = []
B = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    A.append(a)
    B.append(b)

print((max(A)-min(A))*(max(B)-min(B)))