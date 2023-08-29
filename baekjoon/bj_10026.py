import sys
input = sys.stdin.readline
from collections import deque

n =int(input())
graph = [list(input().strip('\n')) for _ in range(n)]
visited = [[0]*(n)  for _ in range(n)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited[x][y]=1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] == graph[x][y]:
                    visited[nx][ny] =1
                    q.append((nx, ny))

cnt1, cnt2 =0,0

#적록색약이 아닐 때
for i in range(n):
    for j in range(n):
         if not visited[i][j]:
             bfs(i, j)
             cnt1 +=1
             
#적록색약일 때
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[0]*(n)  for _ in range(n)]            
#적록색약일 때
for i in range(n):
    for j in range(n):
         if not visited[i][j]:
             bfs(i, j)
             cnt2 +=1

print(cnt1,cnt2)