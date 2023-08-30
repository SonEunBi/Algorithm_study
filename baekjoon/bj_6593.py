import sys
input = sys.stdin.readline
from collections import deque
l, r, c = map(int, input().split())
graph=[[0]*r for _ in range(r)]
for k in range(l):
    for i in range(r):
        graph = list(input().split() for _ in range(r))
        
print(graph)
for k in range(l):
    for i in range(r):
        for j in range(c):
            if graph[i][j] == '.':
                graph[i][j] = k+1

visited =[[0]*(c) for _ in range(r)]
flag, cnt  =0, 0

def bfs(x, y):
    global cnt
    q = deque()
    q.append((x,y))
    visited[x][y] =1
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    while q:
        if graph[x][y] == 'E':
            return 0
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<= nx < 30 and 0 <=ny <30 and not visited[nx][ny] or (visited[nx][ny] == visited[x][y]+1):
                cnt +=1
                visited[nx][ny]
                q.append((nx, ny))
    return (1, cnt)    
cnt2 =0
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'S':
            flag, cnt2 = bfs(i, j)
            
if flag == 1:
    print('Trapped!')
else:
    print('Escaped in ',cnt2, 'minute(s)')
