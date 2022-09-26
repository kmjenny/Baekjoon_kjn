# 나는 요리사다
import sys
all = []
for i in range(5):
    sum = 0
    score = list(map(int,sys.stdin.readline().split()))
    for i in score:
        sum += i
    all.append(sum)
for i in range(5):
    if max(all)==all[i]:
        print(i+1, end=" ")
print(max(all))