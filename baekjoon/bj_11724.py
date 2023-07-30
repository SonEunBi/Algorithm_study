import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph=[[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt =0
def dfs(i):
    stack=[]
    stack.append(i)
    visited[i] =True
    while stack:
        now = stack.pop()
        for nxt in graph[now]:
            if not visited[nxt]:
                stack.append(nxt)
                dfs(nxt)

for i in range(1, n+1):
    if not visited[i]:
        cnt+=1
        dfs(i)
print(cnt)