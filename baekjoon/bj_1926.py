import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())
image = [list(map(int, input().split())) for i in range(n)]
visited =[[False]*m for _ in range(n)]
cnt =0
dx = [1,-1, 0,0]
dy = [0,0,1,-1]

def bfs(x, y):
    width =1
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if image[nx][ny]==1 and not visited[nx][ny]:
                    visited[nx][ny] =True
                    q.append((nx, ny))
                    width +=1
    return width

ans = 0
for i in range(n):
    for j in range(m):
        if image[i][j] == 1 and not visited[i][j]:
            cnt +=1
            ans = max(bfs(i,j), ans)
            
print(cnt)
print(ans)
        
        