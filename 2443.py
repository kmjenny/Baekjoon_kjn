# 별 찍기-6
N = int(input())

for i in range(N,0,-1):
    print('{0}{1}'.format(' '*(N-i),'*'*(2*i-1)))