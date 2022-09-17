# 별 찍기-5
N = int(input())

for i in range(1,N+1):
    print('{0}{1}'.format(' '*(N-i),'*'*(2*i-1)))