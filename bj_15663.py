import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
tmp = []
visited =[False for _ in range(1000001)]
ans =[]
def dfs(start):
    if len(tmp) == m:
        ans.append(tmp[:])
        return
    
    for i in range(n):
        if not visited[i]:
            tmp.append(num[i])
            visited[i]=True
            dfs(num[i])
            visited[i]=False
            tmp.pop()
dfs(0)
ans = sorted(list(set(map(tuple, ans))))
for i in ans:
    print(*i, sep=' ')