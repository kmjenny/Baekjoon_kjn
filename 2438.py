# 별 찍기-1
N = int(input())

for i in range(N):
    for j in range(i+1):
        print("*", end="")
    print('')

# 간단한 코드
for i in range(N):
    print('{:}'.format('*'*(i+1)))