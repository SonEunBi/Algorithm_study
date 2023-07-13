import sys
input = sys.stdin.readline

n,m = map(int, input().split())
visited =[[0] for i in range(n)]
def dfs(start, end):
    start, end = map(int, input().split())
    for i in range(m):
        visited[start] =1
        visited[end]=1
    
    