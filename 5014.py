# 5014
# 스타트링크
import sys
from collections import deque

# 총 f층 / 지금 위치 s층 / 목적지 g층
# 위로 u층 이동 -> U 버튼 / 아래로 d층 이동 -> D 버튼
# 이동 불가능하면 use the stairs
f, s, g, u, d = map(int, sys.stdin.readline().split())

def bfs(f, s, g, u, d):
    queue = deque([(s,0)])
    visited = set([s])

    while queue:
        x, dist = queue.popleft()

        if x == g:
            return dist

        for nx in (x+u, x-d):
            if 1 <= nx <= f and nx not in visited:
                queue.append((nx, dist+1))
                visited.add(nx)

    return "use the stairs"

print(bfs(f,s,g,u,d))