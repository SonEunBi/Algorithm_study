import sys
input = sys.stdin.readline

t=int(input())
def dfs(a, cnt):
    visited[a]=1
    
    for i in graph[a]:
        if not visited[i]:
            cnt = dfs(i, cnt+1)
    return cnt
                
                
for _ in range(t):
    cnt =0
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    visited =[0]*(n+1)
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
   

    print(dfs(1, 0)) 