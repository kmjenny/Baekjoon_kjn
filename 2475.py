# 검증수
import sys
sum = 0
a = list(map(int, sys.stdin.readline().split()))
for i in range(5):
    sum += a[i]*a[i]
print(sum%10)
