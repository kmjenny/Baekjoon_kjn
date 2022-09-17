# 완전제곱수

M=int(input())
N=int(input())
sum=0
check=0
min_one=0

for i in range(M,N+1):
    for j in range(1,i+1):
        if j*j==i:
            sum = sum+i
            if check==0:
                min_one=i
                check=1
            break

if check==0:
    print('-1')
else:
    print(sum)
    print(min_one)