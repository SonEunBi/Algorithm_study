import sys
input = sys.stdin.readline
 
n, m = map(int, input().split())
num = sorted(map(int, input().split()))
 
tmp = []
visited =[False for _ in range(1000001)]
 
def dfs():
    if len(tmp) == m:
        print(' '.join(map(str, tmp)))
        return
    
    for i in num:
        if not visited[i]:
            tmp.append(i)
            visited[i] = True
            dfs()
            tmp.pop()
            visited[i] = False
dfs()