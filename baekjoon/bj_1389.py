import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited =[False for _ in range(n+1)]
lv =[]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(i, cnt):
    q = deque()
    q.append(i)
    while q:
        x = q.popleft()
        visited[x] =True
        for nxt in graph[x]:
            if not visited[nxt]:
                visited.append(nxt)
                q.append(nxt)
                lv[nxt] = lv[x]+1
    

    
bfs(1 , 0)