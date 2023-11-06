import sys
input = sys.stdin.readline
cnt =0
n,m = map(int, input().split())
graph=[[0]*n for i in range(n)]
answer= [0 for i in range(n)]
for i in range(n):
    a,b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
    
for i in range(0,n):
    for j in range(0, n):
        if graph[i][j] == 1:
            i = j
            cnt +=1
        if i==j:
            answer.append(cnt)
            cnt =0