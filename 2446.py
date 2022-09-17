# 별 찍기-9
N=int(input())
for i in range(N,1,-1):
    print('{0}{1}'.format(' '*(N-i),'*'*(2*i-1)))
for i in range(1,N+1):
    print('{0}{1}'.format(' '*(N-i),'*'*(2*i-1)))