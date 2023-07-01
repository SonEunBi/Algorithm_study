import sys
input = sys.stdin.readline

n = int(input())
dx = [1,-1,0,0]
dy = [0,0,1,-1]

cnt =0
board =[list(map(int,input().rstrip())) for _ in range(n)]
visited = []*(n+1)

ans = []
result =0
def dfs(x, y):

    if x <0 or x>=n or y<0 or y>=n:
        return
    
    if board[x][y] == 1:
        global cnt
        cnt+=1
        board[x][y]=0
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            dfs(nx,ny)
        return True
    return False
        
            
for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            ans.append(cnt)
            result +=1
            cnt =0
        
ans.sort()
print(result)
print("\n".join(map(str, ans)))
            
        
    
    