# 별 찍기-7
N=int(input())
for i in range(1,N):
    print('{0}{1}'.format(' '*(N-i),'*'*(2*i-1)))
for i in range(N,0,-1):
    print('{0}{1}'.format(' '*(N-i),'*'*(2*i-1)))