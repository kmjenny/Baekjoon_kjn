# 점수 집계
import sys
T = int(sys.stdin.readline())
all = []
for i in range(T):
    score = list(map(int,sys.stdin.readline().split()))
    score.remove(max(score))
    score.remove(min(score))
    if max(score)-min(score)>=4:
        all.append('KIN')
    else:
        all.append(sum(score))
for i in all:
    print(i)
