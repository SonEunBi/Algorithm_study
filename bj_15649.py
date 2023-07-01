import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tmp = []
visited =[False for _ in range(101)]

def dfs():
    if len(tmp) == m:
        print(' '.join(map(str, tmp)))
        return
    
    for i in range(1, n+1):
        if not visited[i]:
            tmp.append(i)
            visited[i] = True
            dfs()
            tmp.pop()
            visited[i] = False
dfs()