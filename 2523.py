# 별 찍기-13
N=int(input())
for i in range(1,N+1):
    print("{:}".format("*"*i))
for i in range(N-1,0,-1):
    print("{:}".format("*"*i))