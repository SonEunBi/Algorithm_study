def solution(rect, chrX, chrY, itemX, itemY):
    #rect = 상자 위치, chr x, y = 초기 위치, item x,y = 아이템 위치
    answer = 0
    chrX,chrY, itemX, itemY = 2*chrX, 2*chrY, 2*itemX, 2*itemY
    graph = [[2]*101 for i in range(101)]
    visited = [[0]*len(rect) for i in range(len(rect))]
    for lx, ly, rx, ry in rect:
        
            lx, ly, rx, ry = 2*lx, 2*ly, 2*rx, 2*ry #2배씩 크기 늘려주기
            for x in range(lx, rx+1): #x그리기
                graph[ly][x] = 1
                graph[ry][x]=1
            for y in range(ly, ry+1): #y그리기
                graph[y][lx] = 1
                graph[y][rx]=1
                
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    cnt =0
    def dfs(x, y):
        visited[y][x] =1
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx < 100 and 0<= ny < 100:
                if not visited[ny][nx] and graph[ny][nx]:
                    visited[ny][nx] =1
                    cnt +=1
            
    
    dfs(chrX, chrY)
        
    return answer

rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
cX, cY, iX, iY = 1, 3, 7, 8

solution(rectangle, cX, cY, iX, iY)

a = [1 ,2]
x, y = a
