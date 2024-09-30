# 2667
# 단지번호붙이기
import sys
from collections import deque

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    homes[x][y] = 0

    w = 1
    q = deque()
    q.append([x, y])

    while q:
        i, j = q.popleft()

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if 0<=nx<n and 0<=ny<n and homes[nx][ny] == 1:
                q.append((nx, ny))
                homes[nx][ny] = 0;
                w += 1
    return w

n = int(sys.stdin.readline())
homes = []

for _ in range(n):
    home = list(map(int, sys.stdin.readline().rstrip()))
    homes.append(home)

answer = []
cnt = 0
for i in range(n):
    for j in range(n):
        if homes[i][j]:
            cnt += 1
            answer.append(bfs(i, j))

print(cnt)
answer = sorted(answer)

for i in answer:
    print(i)