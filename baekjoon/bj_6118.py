import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph =[[] for _ in range(n+1)]
visited =[0 for _ in range(n+1)]
depth = [0]*(n+1)
num = []
for _ in range(m):
    a, b =  map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(x):
    q= deque()
    q.append(x)    
    while q:
        barn = q.popleft()
        for i in graph[barn]:
            if not visited[i]:
                visited[i] =1
                q.append(i)
                depth[i] = depth[barn]+1
bfs(1)
depth[1] =0
cnt =0
for i in range(len(depth)):
    if max(depth) == depth[i]:
        num.append(i)
        cnt+=1
print(num[0], max(depth), cnt)
                
        
        