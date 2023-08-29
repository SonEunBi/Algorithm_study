import sys
input = sys.stdin.readline
from collections import deque

m, n , k = map(int, input().split())
graph = [[0]*(n) for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1,y2):
        for j in range(x1, x2):
            graph[i][j] +=1

def bfs(y, x):
    cnt2=1
    q = deque()
    q.append((y, x))
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while q:
        y,x = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<= nx < n and 0 <= ny < m:
                if graph[ny][nx] == 0: 
                    graph[ny][nx] =1
                    q.append((ny, nx))
                    cnt2 +=1
    return cnt2

arr =[]   
cnt =0
for i in range(m):
    for j in range(n):
        if graph[i][j] ==0:
            graph[i][j] +=1
            cnt+=1
            arr.append(bfs(i, j))
            
arr.sort()
print(cnt)
print(' '.join(map(str, arr)))