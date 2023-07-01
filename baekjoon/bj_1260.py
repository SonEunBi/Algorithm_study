import sys
from collections import deque
input = sys.stdin.readline

n, m , v = map(int, input().split())
board =[[False]*(n+1) for _ in range(n+1)]
visited1 = [False]*(n+1)
visited2= [False]*(n+1)

for i in range(m):
    a, b = map(int, input().split())
    board[a][b] = True
    board[b][a] =True
    
def dfs(v):
    visited1[v] =True
    print(v, end = " ")
    for i in range(1, n+1):
        if not visited1[i] and board[v][i]:
            dfs(i)
            
            
def bfs(v):
    deq = deque([v])
    visited2[v] = True
    
    while deq:
        v = deq.popleft()
        print(v, end=" ")
        for i in range(1, n+1):
            if not visited2[i] and board[v][i]:
                deq.append(i)
                visited2[i]=True
                
            
dfs(v)
print()
bfs(v)