from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())#n개의 세로, m개의 가로
board = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
q=deque()
q.append([0,0])
cnt =0 
while q:
    y,x =q.popleft()
    
    for i in range(4):    
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or nx>=m or ny<0 or ny>=n:
            continue
        
        if board[ny][nx]==1:
            q.append([ny, nx])
            board[ny][nx] = board[y][x]+1

print(board[n-1][m-1])