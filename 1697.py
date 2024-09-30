# 1697
# 숨바꼭질

import sys
from collections import deque

def bfs(n, k):
    queue = deque([(n, 0)])
    visited = set([n])

    while queue:
        x, dist = queue.popleft()

        if x == k:
            return dist
        
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and nx not in visited:
                queue.append((nx, dist+1))
                visited.add(nx)
    
    return -1

MAX = 10 ** 5
n, k = map(int, sys.stdin.readline().split())

print(bfs(n,k))