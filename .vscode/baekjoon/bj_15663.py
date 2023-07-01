import sys
input = sys.stdin.readline
 
n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
tmp = []
visited =[False for _ in range(1000001)]
 
def dfs():
    start =0
    if len(tmp) == m:
        print(*tmp)
        return
 
    for i in range(n):
        if not visited[i] and start != num[i]:
            tmp.append(num[i])
            visited[i]=True
            start = num[i]
            dfs()
            visited[i]=False
            tmp.pop()
dfs()