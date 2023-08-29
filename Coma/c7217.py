import sys
input = sys.stdin.readline
from collections import deque

end, start = map(int,input().split())
dp = [100001]*(100001)
dp[start] =0

def bfs(start):
    q = deque()
    q.append(start)
    while q:
        x = q.popleft()
        if x==end:
            print(dp[end])
            break
        for nx in (x+1, x-1, x*2):
            if 0<= nx <= 100000 and dp[nx]== 100001:
                dp[nx] = dp[x]+1
                q.append(nx)
bfs(start)