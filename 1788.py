# 1788
# 피보나치 수의 확장
# 실버 3
import sys

n = int(sys.stdin.readline())
num = abs(n)
f = [0] * (num+1)
f[0] = 0

if num > 0:
    f[1] = 1
    for i in range(2, num+1):
        f[i] = (f[i-2] + f[i-1])%1000000000

if n == 0:
    print(0)
elif n < 0 and num%2==0:
    print(-1)
else:
    print(1)

print(f[num])