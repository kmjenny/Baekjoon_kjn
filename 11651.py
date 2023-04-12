# 좌표 정렬하기 2
# 실버5
import sys
N = int(sys.stdin.readline())
dot = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    dot.append((x,y))

result = sorted(dot, key=lambda x : (x[1],x[0]))
for i in result:
    for j in i:
        print(j, end=" ")
    print()