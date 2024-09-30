import sys
from collections import deque

def bfs(x, y):
    ground[x][y] = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    q.append([x,y])
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<n and 0<=ny<m and ground[nx][ny] == 1:
                q.append([nx, ny])
                ground[nx][ny] = 0

T = int(sys.stdin.readline())

for i in range(T):
    m, n, k = map(int, sys.stdin.readline().split())
    ground = [[0 for a in range(m)] for b in range(n)]
    ans = 0
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        ground[y][x] = 1
    
    for a in range(n):
        for b in range(m):
            if ground[a][b] == 1:
                ans += 1
                bfs(a, b)
    
    print(ans)
    