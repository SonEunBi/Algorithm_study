import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
com = [[] for i in range(n+1)]
visited =[0]*(n+1)
start =0
ans =[]

for i in range(m):
    a,b = map(int, input().split())
    com[a].append(b)
    com[b].append(a)

cnt =0

def dfs(v):
    global cnt
    visited[v]=True
    for i in com[v]:
        if not visited[i]:
            cnt+=1
            dfs(i)
    return cnt

print(dfs(1))