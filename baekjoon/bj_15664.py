import sys
input = sys.stdin.readline
 
n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
tmp =[]
visited=[False for i in range(10000001)]
 
def dfs(start):
    if len(tmp) == m:
        print(' '.join(map(str, tmp)))
        return
    prev =0
    
    for i in range(n):
        if not visited[i] and prev != num[i] and start <= num[i]:
            visited[i] = True
            tmp.append(num[i])
            prev = num[i]
            dfs(num[i])
            tmp.pop()
            visited[i] = False
dfs(0)