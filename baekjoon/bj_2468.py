import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
board = [list(map(int, input().split())) for i in range(n)]

def dfs(x, y, h):
    dx = [1, -1, 0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < n and 0<= ny < n and board[nx][ny] > h and not visited[nx][ny]:
            visited[nx][ny]=1
            dfs(nx, ny, h)
            
answer = 1
for k in range(1, 101):
    visited = [[0]*n for _ in range(n)]
    cnt =0
    for i in range(n):
        for j in range(n):
            if board[i][j] > k and not visited[i][j]:
                cnt+=1
                visited[i][j]=1
                dfs(i, j, k)
    answer = max(cnt, answer)

print(answer)