import sys
input = sys.stdin.readline
from collections import deque

total,now,dst,u,d= map(int, input().split())
visited = [False for _ in range(total+1)]
cnt = [0 for _ in range(total+1)]

def bfs(s):
    q = deque()
    q.append(s)
    visited[s]=True
    while q:
        s = q.popleft()
        if s == dst:
            return cnt[dst]
        for dm in (s + u, s-d):
            if 1 <= dm <=total and not visited[dm]:
                visited[dm]= True
                cnt[dm] = cnt[s]+1
                q.append(dm)
    if cnt[dst] == 0:
        return 'use the stairs'
        
print(bfs(now))
