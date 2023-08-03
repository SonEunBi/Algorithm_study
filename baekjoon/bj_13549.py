import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
cnt =0
def bfs(now):
    q = deque()
    q.append(now)
    while q:
        now = q.popleft()
        if now == k:
            return cnt
        for i in (now-1, now+1, 2*now):
            di = now + i
            q.append(di)
        print(q)
print(bfs(n))