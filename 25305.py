# 커트라인
# 브론즈2
import sys
N, k = map(int, sys.stdin.readline().split())
score = list(map(int, sys.stdin.readline().split()))

score.sort(reverse=True)
print(score[k-1])