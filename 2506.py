# 점수계산
import sys
N = int(sys.stdin.readline())
problems = list(map(int,sys.stdin.readline().split()))
if problems[0]==1:
    count = 1
    sum = 1
else:
    count = 0
    sum = 0
for i in range(1,N):
    if problems[i]==1:
        count += 1
        sum = sum + count
    else:
        count = 0
print(sum)