import sys
from collections import deque
input = sys.stdin.readline

row, col  = map(int, input().split())
board =[]
for i in range(row):
    
visited = [False for i in range(10001)]

dx =[1, -1, 0,0]
dy = [0,0,1,-1]

def dfs(x, y):
    for y in range(row):
        for x in range(col):
            if not visited[i]:
                dx = x + dx
                dy = y + dy
            
dfs(0,0)