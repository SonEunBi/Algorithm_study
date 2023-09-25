import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [list(input()) for _ in range(5)]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs(graph):
    n_graph =[['0']*5 for _ in range(5)] #계속 그래프 새로 그려줌
    for i in range(5):
        for j in range(5):
            cnt =0
            for k in range(8): #8가지 방향 모두 확인
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < 5 and 0 <= ny < 5 and graph[nx][ny] == '1':
                    cnt += 1
            res = cnt
            if graph[i][j] =='1':
                if res in [2,3]: #살아있는 상태인데 살 수 있으면
                    n_graph[i][j] ='1'
            else:
                if res ==3: #죽어있는 상태인데 살아날 수 있으면
                    n_graph[i][j] ='1'

    return n_graph


for _ in range(n):
    graph = bfs(graph)
    
for i in graph:
    print(''.join(i))
                        
                    
                    