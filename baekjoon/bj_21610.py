import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
lst =[]
q = deque()
for i in range(m):
    #1칸씩 줄여서 계산해야 함. 첫칸이 (1,1)
    d,s = map(int, input().split())
    q.append((d,s))
cloud = [(n,1), (n,2), (n-1,1),(n-1,2)]
direct = [(-1,0), (-1,1), (0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def move(x, y):
    while q:
        x, y = q.popleft()
        for i in range(m):
            nx = (x+direct[i][0]*s)%n
            ny = (y+direct[i][1]*s )%n
            if 0<=nx < n and 0<= ny < n:
                graph[nx][ny] +=1

    