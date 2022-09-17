# OX 퀴즈

N = int(input())
all_score = []

for i in range(N):
    result = list(input())
    score = 0
    k = 0
    for j in range(len(result)):
        if j==0 and result[j]=='O':
            score +=1
            k += 1
        else:
            if result[j]=='O':
                score = score+1+k
                k += 1
            elif result[j]=='X':
                k = 0
    all_score.append(score)

for i in all_score:
    print(i)