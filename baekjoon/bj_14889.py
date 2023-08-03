import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().rstrip().split())) for i in range(n)]
ability = [[0]*(n) for i in range(n)]
visited = []
ans =200
for i in range(len(graph)):
    for j in range(len(graph)):
        ability[i][j] = graph[i][j] + graph[j][i]
start =0
link =0
def dfs(i):
    stack = []
    stack.append(i)
    for i in range(n):
        for j in range(n):
            start = ability[i][j] + ability[j][i]
            visited[i] =1
            visited[j] =1
            if not visited:
        
print(ans)