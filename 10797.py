# 10부제
import sys
dates = int(sys.stdin.readline())
car = list(map(int,sys.stdin.readline().split()))
count=0
for i in range(5):
    if car[i]%10==dates:
        count += 1
print(count)