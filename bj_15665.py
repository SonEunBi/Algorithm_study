import sys
input = sys.stdin.readline
 
n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
tmp =[]
 
def dfs():
    if len(tmp) == m:
        print(' '.join(map(str, tmp)))
        return
    prev =0
    
    for i in range(n):
        if prev != num[i]:
            tmp.append(num[i])
            prev = num[i]
            dfs()
            tmp.pop()
dfs()