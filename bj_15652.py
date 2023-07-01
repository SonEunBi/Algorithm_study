import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tmp = []

def dfs(start):
    if len(tmp) == m:
        print(' '.join(map(str, tmp)))
        return
    
    for i in range(start, n+1):
            tmp.append(i)
            dfs(i)
            tmp.pop()
dfs(1)