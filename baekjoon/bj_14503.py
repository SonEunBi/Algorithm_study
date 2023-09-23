import sys
input = sys.stdin.readline
from collections import deque

graph= []
n, m =map(int, input().split())
r,c,d = map(int, input().split())
graph : list =[list(map(int,input().split())) for _ in range(n)]
dy :list =[-1,0,1,0]
dx :list = [0,1,0,-1]
def val(ny, nx):
    return 0<=nx<m and 0<=ny <n 

#서 남 동 북
#0 3 2 1

#만약 후진하려면 
#서쪽을 보고 있으면 x +1, y #거꾸로 해주면 됨
#동쪽으로 후진은 x -1, y
def bfs(y:int,x:int,d:int):
    res =1
    q = deque()
    q.append((y,x,d))
    graph[y][x] =2
    while q:
        y,x,d =q.popleft()
        for i in range(4):
            d = (d-1)%4
            nx = dx[d]+x
            ny = dy[d]+y
            if val(ny,nx) and not graph[ny][nx]: #청소되지 않은 빈 칸이 있는 경우
                res +=1
                graph[ny][nx] =2
                q.append((ny,nx,d))
                break
            
        else: #사방을 다 청소했을 때
            ny, nx = y-dy[d], x -dx[d] #후진
            if graph[ny][nx] ==1:
                return res
                
            q.append((ny,nx,d))
            
                
print(bfs(r,c,d))


            