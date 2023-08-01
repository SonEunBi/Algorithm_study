import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
visited =[0 for _ in range(n+1)]
acq =[[]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    acq[a].append(b)
    acq[b].append(a)
    
visited[1] = 1
def dfs(i, depth):
    if depth == 2:
        return
    for j in acq[i]:
        if not visited[j]:
            visited[j] = 1
        dfs(j, depth +1)
        
        
dfs(1, 0)
visited[1] =0
print(sum(visited))
