import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
dp = [[0]*(n+1) for i in range(m+1)]
wood = [map(int, input().split()) for i in range(n)]

def bfs(start):
    q = deque()
    q.append(start)
    while q:
        x = q.popleft()
        for nx 