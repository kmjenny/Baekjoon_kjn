# 도미노
N = int(input())
point = 0
for i in range(1,N+1):
    point += i*(i+1)
    for j in range(1,i+1):
        point += j
print(point)
