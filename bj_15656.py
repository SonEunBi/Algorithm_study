import sys
input = sys.stdin.readline
 
n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
tmp = []
visited =[False for _ in range(1000001)]
def dfs():
    if len(tmp) == m:
        print(' '.join(map(str, tmp)))
        return
    
    for i in range(n):
            tmp.append(num[i])
            visited[i] = True
            dfs()
            tmp.pop()
            visited[i] = False
            
dfs()