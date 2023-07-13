import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int,input().rstrip())) for i in range(n)]
answer =[]
cnt =0

def dfs(x, y):
    global cnt
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    board[x][y]=0
    cnt+=1
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0<= nx < n and 0<= ny< n and board[nx][ny]==1:
            dfs(nx,ny)
            
    return cnt
    
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            cnt =0
            dfs(i, j)
            answer.append(cnt)
print(len(answer))
answer.sort()
print('\n'.join(map(str, answer)))
        
    