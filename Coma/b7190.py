import sys
input = sys.stdin.readline
from collections import deque

MAX = 10**5
a,b = map(int, input().split())
dist = [0 for i in range(MAX)]
def bfs(a):
    cnt =0
    q = deque()
    q.append(a)
    while q:
        y = q.popleft()
        if y == b:
            print(dist[b])
            break
        for ny in (y+3, y-1):
            if 1<=ny <=MAX and not dist[ny]:
                dist[ny] = dist[y]+1
                q.append(ny)
bfs(a)