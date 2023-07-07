import sys
input = sys.stdin.readline

n = int(input())
nlist=[]
tmp =[]
for i in range(1, n+1):
    nlist.append(i)

def dfs(v):
    if n == len(tmp):
        print(' '.join(map(str, tmp)))
        return 
    for i in range(1, n+1):
        if i not in tmp:
            tmp.append(i)
            dfs(i)
            tmp.pop()
dfs(nlist[0])

    