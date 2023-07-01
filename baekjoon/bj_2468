from collections import deque
import sys
read = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0,0]

n = map(int, read().split())
graph=[[0]*(n+1) for _ in range(n+1)]
visited=[0]*(n+1)

for _ in range(n):
    a, b = map(int, read().split()) 
    graph[a][b] = 1
    graph[b][a] =1
    
chk =0
water =0
def dfs(x, y):
    global chk
    chk += 1
    for i in range(4):
        dx = x + x[i]
        dy = y + y[i]
        dfs(dx, dy)
    return True

for i in range(n):
    for j in range(n):
        if dfs(i, j)==True:
            
            
            