from collections import deque
import sys
read = sys.stdin.readline()
sys.setrecursionlimit(10**7)

a, b, k = map(int, read().rstrip().split())
graph = [[0]*(b+1) for _ in range(a+1)]
visited = [[0]*(b+1)for _ in range(a+1)]
answer = []

dx = [0,0,1,-1]
dy = [1,-1,0,0]

for _ in range(k):
    r, c = map(int, read().strip())
    graph[r-1][c-1] = 1

def dfs(x, y):
    visited[x][y] =1
    global cnt
    cnt+=1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >=0 or nx<a or ny >=0 or ny <b:
            if graph[nx][ny] ==1 and visited[nx][ny]==0:
                dfs(nx, ny)
    return cnt

for i in range(a):
    for j in range(b):
        if graph[i][j] ==1 and visited[i][j]==0:
            cnt =0
            answer.append(dfs(i,j))
            
print(max(answer))