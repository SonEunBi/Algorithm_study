import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph =[[] for _ in range(n+1)]
depth =[1 for _ in range(n+1)]
ans = []*(n+1)
res =[]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(x):
    visited = [0]*(n+1)
    visited[x] =1
    q= deque()
    q.append(x)
    cnt =1
    while q:
        i = q.popleft()
        for j in graph[i]:
            if not visited[j]:
                cnt+=1
                visited[j] =1
                q.append(j)
    return cnt
                
            
for i in range(1,n+1):
    ans.append(bfs(i))
    
for k in range(n):
    if max(ans) == ans[k]:
        res.append(k+1)
print(' '.join(map(str,res)))