import sys
input = sys.stdin.readline
 
n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
tmp = []
visited =[False for _ in range(1000001)]
def dfs(start):
    if len(tmp) == m:
        print(' '.join(map(str, tmp)))
        return
    
    for i in range(n):
        if not visited[i] and start < num[i]:
            tmp.append(num[i])
            visited[i] = True
            dfs(num[i])
            tmp.pop()
            visited[i] = False
            
dfs(0)