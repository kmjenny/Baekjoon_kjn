# 주사위 게임

n = int(input())
score_a = 100
score_b = 100

for i in range(n):
    a, b=map(int, input().split())
    if a<b:
        score_a -= b
    elif a>b:
        score_b -= a

print(score_a)
print(score_b)