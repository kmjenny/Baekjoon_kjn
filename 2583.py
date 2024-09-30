# 2583
# 영역 구하기
import sys
from collections import deque

def bfs(start_x, start_y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    graph[start_x][start_y] = 0

    w = 1
    queue = deque()
    queue.append([start_x, start_y])

    while queue:
        p, q = queue.popleft()

        for k in range(4):
            nx = p + dx[k]
            ny = q + dy[k]

            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny]==1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                w += 1
    return w

m, n, k = map(int, sys.stdin.readline().split())
graph = [[1]*n for _ in range(m)]

for _ in range(k):
    a, b, x, y = map(int, sys.stdin.readline().split())
    for i in range(b, y):
        for j in range(a, x):
            graph[m-i-1][j] = 0

answer = []
cnt = 0
for i in range(m):
    for j in range(n):
        if graph[i][j]:
            cnt += 1
            answer.append(bfs(i, j))

print(cnt)
answer = sorted(answer)

for i in answer:
    print(i, end=" ")