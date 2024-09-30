# 2178
# 미로 탐색

import sys
from collections import deque

def bfs(n, m, maze):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited = set([(0, 0)])
    queue = deque([(0, 0, 1)])

    while queue:
        x, y, dist = queue.popleft()

        if x == n-1 and y == m-1:
            return dist
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if (nx, ny) not in visited:
                    if maze[nx][ny] == 1:
                        visited.add((nx, ny))
                        queue.append((nx, ny, dist+1))
    
    return -1

n, m = map(int, sys.stdin.readline().split())
maze = []

for _ in range(n):
    a = list(map(int, sys.stdin.readline().rstrip()))
    maze.append(a)

print(bfs(n,m,maze))