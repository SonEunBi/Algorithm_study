import sys
input = sys.stdin.readline
from collections import deque

dr = [[-1,0],[-1,0],[0,1],[0,1]]
dc =  [[0,-1],[0,1],[1,0],[-1,0]]
# 0   1   2   3
#  *  *   **  **
# **  **   *  *
visited = [[0]*5 for _ in range(5)]
a =[[0]*5 for _ in range(5)]
n,m =0,0
totalIterCnt, res = 0, -1
def inRange(r, c, R, C): #중심점 (r,c)
    return 0 <= r < R and 0 <= c < C
#(r,c)를 중심으로 하는 d번 케이스의 부메랑
#(r,c)를 포함하여 3개의 좌표가 보드 안에 존재해야 한다
def dfs(cord, cur, cand):
    #뽑은 좌표 목록을 통해 실제로 부메랑을 배치시켜보며 문제에서 요구하는 답을 갱신할 것임
    global res
    global totalIterCnt
    #cord를 cur개의 좌표들에 부메랑을 성공적으로 배치했을 때 얻을 수 있는 가중치 합이 cand라면
    #cur은 중심의 개수라고 볼 수 있음
    if cur == len(cord):
        #추출한 모든 좌표에 대해 각 좌표를 부메랑의 중심으로 여기고 배치할 수 있으면 케이스 찾음
        res = max(res, cand)
        return res
    r= cord[cur]//m #행
    c= cord[cur]%m #열
    #r*m + c번 좌표
    if not visited[r][c]:
        for i in range(4):
            totalIterCnt+=1
            nr1, nc1 = r+dr[i][0],c+dc[i][0]            
            if not inRange(nr1,nc1, n,m) or visited[nr1][nc1]:
                continue  
            nr2, nc2 = r+dr[i][1],c+dc[i][1]
            if not inRange(nr2,nc2,n,m) or visited[nr2][nc2]:
                continue
            
            visited[r][c] = visited[nr1][nc1] = visited[nr2][nc2] =1 
            #가중치 = 중심*2+가중치+날개1+날개2
            dfs(cord, cur+1, cand+a[r][c]*2 + a[nr1][nc1] + a[nr2][nc2])
            
            #다시 초기화
            visited[r][c] = visited[nr1][nc1] = visited[nr2][nc2] =0

#n*m 보드에서 k개의 좌표를 선택하는 모든 경우의 수를 추출
#cord : 지금까지 뽑은 좌표 목록 #last~k까지 뽑기
def choose(last, k, cord):
    global totalIterCnt
    if (not k) or (last == n*m):
        if not k: #k가 0이면
            dfs(cord, 0,0)
        return
    #last+1부터 k개의 좌표를 선택     
    #last 현재 좌표, k는 선택 가능한 남은 좌표, cord는 선택한 좌표들
    
    #k는 최소를 선택했음
    #현재 좌표 x, 다음 좌표 선택
    choose(last+1, k, cord)
    #현재 좌표 선택하고 cord에 추가하기
    cord.append(last)
    #현재 좌표 선택, 선택 가능좌표 -1
    choose(last+1, k-1, cord)
    cord.pop()
    #현재 좌표를 선택하지 않은 상태로 되돌리기
    totalIterCnt+=1

n, m =map(int, input().split())
a =[list(map(int, input().split())) for _ in range(n)]
#최대가 8이고, 5*5도 8보다는 작음
for i in range(min(8, m*n//3), -1, -1):
    v= []
    choose(0, i, v)
    v.clear()
    if res != -1:
        break
print(res)
    