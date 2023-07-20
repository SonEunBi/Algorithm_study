import sys
input = sys.stdin.readline

graph = [list(input().split()) for i in range(5)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
ans =set()   
def dfs(x, y, res): 
    if len(res) == 6:
        ans.add(res)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < 5 and 0<= ny < 5:
            dfs(nx, ny, res + graph[nx][ny])

    
for i in range(5):
    for j in range(5):
        res = graph[i][j]
        dfs(i,j, res)
print(len(ans))
        
        
    