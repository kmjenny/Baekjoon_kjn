# 7562
# 나이트의 이동
import sys
from collections import deque

def bfs(s_x, s_y, e_x, e_y, l):
    d = [(1,2),(1,-2),(2,1),(2,-1),(-1,2),(-1,-2),(-2,1),(-2,-1)]

    visited = set([(s_x, s_y)])
    queue = deque([(s_x, s_y, 0)])

    while queue:
        x, y, dist = queue.popleft()

        if x == e_x and y == e_y:
            return dist
        
        for i in range(8):
            nx = x + d[i][0]
            ny = y + d[i][1]

            if 0 <= nx < l and 0 <= ny <l:
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, dist+1))

    return -1

t = int(sys.stdin.readline())

for _ in range(t):
    l = int(sys.stdin.readline())
    a, b = map(int, sys.stdin.readline().split())
    x, y = map(int, sys.stdin.readline().split())
    print(bfs(a, b, x, y, l))