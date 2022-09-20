# 평균
import sys
N = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))
max_score = max(score)
sum = 0
for i in range(N):
    score[i] = (score[i]/max_score)*100
    sum += score[i]
print(sum/N)