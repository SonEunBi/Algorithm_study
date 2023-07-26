import sys
from collections import deque
input = sys.stdin.readline

move = [(2,1),(1,2),(2,-1),(1,-2),(-1,2),(-2,1),(-2,-1),(-1,-2)]
t = int(input())

def bfs(x, y):
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        if ex == x and ey == y:
            return board[ex][ey]-1
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0<= nx <size and 0<= ny < size and not board[nx][ny]:
                q.append((nx,ny))
                board[nx][ny] = board[x][y]+1
                
    

for _ in range(t): #테스트
    size = int(input())
    board=[[0]*size for _ in range(size)] #체스판
    x, y = map(int, input().split())
    board[x][y]=1
    ex, ey = map(int, input().split())
    print(bfs(x,y))
    
    
                