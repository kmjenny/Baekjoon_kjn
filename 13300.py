# 13300
# 방 배정
import sys
N, K = map(int, sys.stdin.readline().split())
result = 0

# S 여학생 0, 남학생 1
# Y 학년 1~6
student = [[0,0] for _ in range(6)]

for i in range(N):
    S, Y = map(int, sys.stdin.readline().split())
    student[Y-1][S] += 1

for i in student:
    for j in i:
        if j%K == 0:
            result += (j//K)
        else:
            result += (j//K) + 1

print(int(result))