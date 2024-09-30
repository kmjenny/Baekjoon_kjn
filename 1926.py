import sys
from collections import deque

def bfs(x, y):
    # 0으로 설정해서 방문한 것으로 표시
    # 그래야 아래 main문 if문에서 1인 경우에만 다시 확인할 수 있음
    pics[x][y] = 0
    # 상하좌우 이동 가능한 네 가지 방향 나타냄
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # 이동한 거리 표시(이어진 1의 개수)
    w = 1
    q = deque()
    q.append([x,y])
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            # 상하좌우로 이동한 다음 범위 안인지 & 1인지 확인함
            if 0<=nx<n and 0<=ny<m and pics[nx][ny] == 1:
                # 방문한 곳이 되니까 0으로 바꾸면서 q에 넣음
                q.append([nx, ny])
                pics[nx][ny] = 0
                w += 1
    
    return w
    

n, m = map(int, sys.stdin.readline().split())
pics = []

for _ in range(n):
    pic = list(map(int, sys.stdin.readline().split()))
    pics.append(pic)

cnt = 0
ans = 0
for i in range(n):
    for j in range(m):
        if pics[i][j] == 1:
            cnt += 1
            ans = max(bfs(i, j),ans)

print(cnt)
print(ans)