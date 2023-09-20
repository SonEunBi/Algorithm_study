import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[1]*n for i in range(n)]
cnt =0
def dfs(x, y):   
    cnt = graph[x][y]
    if x == n-1 and y == n-1:
        return cnt
    for nx, ny in ((1,0), (0,1)):
        if 0<=nx <n and 0<=ny <n:
            if graph[nx][ny] !=0 and not visited[nx][ny]:
                if cnt == 0:
                    dfs(nx, ny)
                cnt -=1 