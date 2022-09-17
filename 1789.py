# 수들의 합
# 입력 S(자연수)
# 출력 N(최댓값)

S = int(input())

count = 0
sum = S
n = 1

for i in range(n,sum+1):
    if sum==0:
        break
    if sum-i>n:
        sum = sum-i
        n += 1
        count += 1
    else:
        count+=1
        break

print(count)