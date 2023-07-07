import sys
input = sys.stdin.readline

n = int(input())
nlist =sorted(list(map(int, input().split())))
visited = [False for _ in range(n)]
ans=0
maxi =0
def dfs(v):
    global maxi
    if v == n:
        now_sum =0
        for i in range(n-1):
            now_sum += abs(nlist[i]-nlist[i+1])
        maxi = max(maxi, now_sum)
        return
    for i in range(n):
        if visited[i] == False:
            visited[i] = True
        
        
    