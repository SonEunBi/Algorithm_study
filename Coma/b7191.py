import sys
from collections import deque

graph = [list(map(int, input().split())) for i in range(9)]
visited =[[0]*9 for i in range(9)]
cnt =0

def bfs(x, y):
    deque = []
    deque.append(x, y)
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    visited[x][y]=1
    while deque:
        x, y = deque.pop()
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if 0<= nx < 8 and 0<=ny<8:
                if graph[nx][ny] =='F' and not visited[nx][ny]:
                    deque.append((nx,ny))
                    visited[nx][ny]=1
for i in range(8):
    for j in range(8):
        if not visited[i][j] and graph[i][j] =='F':
            bfs(i,j)
            cnt +=1
print(cnt)