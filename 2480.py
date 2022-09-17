# 주사위 세개
# 입력 a,b,c(주사위 입력값)

a,b,c=map(int, input().split())

if a==b==c:
    reward = 10000+a*1000
elif a==b or b==c:
    reward = 1000+b*100
elif a==c:
    reward = 1000+a*100
else:
    reward = 100*max(a,b,c)

print(reward)