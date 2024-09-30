# 2468
# 안전 영역
import sys

N = int(sys.stdin.readline().rstrip())
grounds = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

def dfs(x, y, h):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = []
    q.append((x, y))

    while q:
        i, j = q.pop()

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if 0 <= nx < N and 0 <= ny < N:
                if new[nx][ny] == 0 and grounds[nx][ny] > h:
                    q.append((nx, ny))
                    new[nx][ny] = 1

ans = 1
for i in range(1, max(map(max, grounds))):
    new = [[0]*N for _ in range(N)]
    cnt = 0
    for x in range(N):
        for y in range(N):
            if new[x][y]==0 and grounds[x][y] > i:
                new[x][y] = 1
                cnt += 1
                dfs(x, y, i)
    if cnt > ans:
        ans = cnt

print(ans)