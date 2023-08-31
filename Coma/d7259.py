import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, time= map(int, input().split())
    graph[a][b] = time
    

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] > graph[i][k]+ graph[k][j]:
                graph[i][j] = graph[i][k]+ graph[k][j]
                
c,d = map(int, input().split())

print(graph[c][d])