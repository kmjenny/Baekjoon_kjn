# 내 학점을 구해줘
import sys
T = int(sys.stdin.readline())
score = []
GPA = []
for i in range(T):
    sum_score = 0
    sum = 0
    N = int(sys.stdin.readline())
    for j in range(N):
        c, g = sys.stdin.readline().split()
        c = int(c)
        g = float(g)
        sum_score += c
        sum += (c*g)
    score.append(sum_score)
    if sum==0:
        GPA.append(0.0)
    else:
        GPA.append(sum/sum_score)
for i in range(T):
    print("{0} {1:.1f}".format(score[i], GPA[i]))
