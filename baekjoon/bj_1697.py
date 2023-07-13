import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
board = [0 for i in range(100000)]

cnt =0
answer= []
def bfs(n):
    q = deque([n])
    while q:
        x = q.popleft()
        if x == k:
            return board[x]
        for nx in (x-1, x+1, 2*x):
            if 0 <= nx <= 100000 and not board[nx]:
                board[nx] = board[x]+1
                q.append(nx)
        

print(bfs(n))
            
        