from collections import deque

def solution(rect, chrX, chrY, itemX, itemY):
    #rect = 상자 위치, chr x, y = 초기 위치, item x,y = 아이템 위치
    answer = 0
    #ㄷ자 형태 조심
    graph = [[0]*101 for i in range(101)]
    for lx, ly, rx, ry in rect:
        lx, ly, rx, ry = 2*lx, 2*ly, 2*rx, 2*ry #2배씩 크기 늘려주기
        for x in range(lx, rx+1): #x그리기
            graph[ly][x] = 1                
            graph[ry][x]=1
        for y in range(ly, ry+1): #y그리기
            graph[y][lx] = 1
            graph[y][rx]=1
    for lx, ly, rx, ry in rect:
        for y in range(ly*2+1, ry*2):
            for x in range(lx*2+1, rx*2):
                graph[y][x] =0
    
    answer = bfs(answer, graph, chrY, chrX, itemY, itemX)
        
    return answer

def bfs(answer, graph, chrY, chrX, itemY, itemX):   
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    cnt =0    
    itemX, itemY = 2*itemX, 2*itemY
    q = deque()
    q.append((chrY*2, chrX*2 , 0))
    while q:
        y,x, cnt = q.popleft()
        if x == itemX and y == itemY:
            answer = cnt //2
            break
        graph[y][x] =0
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx <= 100 and 0<= ny <= 100 and graph[ny][nx] ==1:
                q.append((ny, nx, cnt+1))
    return answer