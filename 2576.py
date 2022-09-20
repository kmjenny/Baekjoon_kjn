# 홀수
import sys
sum = 0
num = []
for i in range(7):
    x = int(sys.stdin.readline())
    if x%2==1:
        sum += x
        num.append(x)
if sum==0:
    print("-1")
else:
    print(sum)
    print(min(num))