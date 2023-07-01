from collections import deque
import sys
read = sys.stdin.readline

a, b = map(int, read().split())

graph = [list(map(int, ' '.join(input().split())))for i in range(a)]

cnt =0

def bfs(x, y):
    queue = deque()
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <0 or nx>=a or ny <0 or ny >=b:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] ==1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx, ny))
    return graph[a-1][b-1]
print(bfs(0,0))