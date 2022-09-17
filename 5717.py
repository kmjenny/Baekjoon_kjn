# 상근이의 친구들
# M: 남자친구의 수 F: 여자친구의 수

M,F=map(int,input().split())
result = []

while M!=0 and F!=0:
    result.append(M+F)
    M, F = map(int, input().split())

for i in result:
    print(i)