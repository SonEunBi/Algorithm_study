import sys
input = sys.stdin.readline

n , m = map(int, input().split())
wood = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
ans =0
#남 서 북 동
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]


def check(y,x, visited, ny, nx, ny2, nx2):
    if visited[ny][nx] == 1 or visited[ny2][nx2] == 1 or visited[y][x] == 1: #하나라도 이미 방문한 경우면 false
        return False
    else:
        visited[y][x] = 1
        visited[ny][nx] = 1
        visited[ny2][nx2] = 1
        return True
        
def dfs(y, x, visited, cnt):
    global ans
    #x, y는 중심임, 중심이 끝에 도달했을 경우 검사
    if x == m: 
        x = 0
        y += 1
    if y == n: 
        ans = max(ans, cnt) #최댓값 구해서 저장
        return
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        ny_, nx_ = y + dy[(i + 1) % 4], x + dx[(i + 1) % 4] #남 서 북 동 (시계방향)순으로 돌 것
        if 0 <= ny < n and 0 <= nx < m and 0 <= ny_ < n and 0 <= nx_ < m:
            if check(y, x, visited, ny, nx, ny_, nx_): #방문 체크
                dfs(y, x + 1, visited, cnt + 2*wood[y][x] + wood[ny][nx] + wood[ny_][nx_])
                visited[y][x] = 0
                visited[ny][nx] = 0
                visited[ny_][nx_] = 0
    dfs(y, x + 1, visited, cnt)

dfs(0, 0, visited, 0)
print(ans)