import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
def bfs(dist, full):
    q = deque()
    q.append((dist,full))
    while q:
        a, b= q.popleft()
        
    

conv = []
for i in range(n):
    dist, full = map(int, input().split())
    conv.append((dist, full))
bfs(0, 0)