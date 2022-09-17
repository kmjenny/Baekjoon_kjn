# 평균 점수
# 입력 5명 학생의 점수

score = list()
score_sum = 0

for i in range(5):
    score.append(input())
    if int(score[i])<40:
        score[i]=40
    score_sum += int(score[i])

print(int(score_sum/5))