import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().rstrip())) for i in range(n)]
#최소의 칸 수 = bfs, queue
q = deque([(0,0)])
dx = [1,-1,0,0]
dy = [0,0,1,-1]
while q:
    y,x=q.popleft()
    for i in range(4):
        nx = dx[i]+x
        ny = dy[i]+y
        if 0<=nx <m and 0<=ny < n and board[ny][nx]==1:
            board[ny][nx] = board[y][x] +1
            q.append([ny,nx])
            
print(board[n-1][m-1])
            
        
        
