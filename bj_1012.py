import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

t = int(input())
dx = [1,-1,0,0]
dy = [0,0,1, -1]

def dfs(x, y):
    if x<0 or x>=m or y<0 or y>=n:
        return
    
    if board[x][y]:
        board[x][y]=False
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            dfs(nx, ny)
        return True
    return False

for _ in range(t):
    m, n, k = map(int,input().split())
    cnt =0
    board = [[False]*m for _ in range(n)]
    
    for _ in range(k):
        a, b = map(int, input().split())
        board[b][a] =True
        
    for i in range(n):
        for j in range(m):
            if dfs(i,j):
                cnt+=1
    print(cnt)





            