import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
puzzle = ''

for i in range(2):
    puzzle += ''.join(list(input().split()))

def bfs():
    global puzzle
    visited = {puzzle:0}
    q = deque([puzzle])
    
    while q:
        puzzle = q.popleft()
        cnt = visited[puzzle]
        
        if puzzle == '123X':
            return cnt
        
        e = puzzle.index('X') 
        x = e // 2 
        y = e % 2        
        cnt += 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < 2 and 0 <= ny < 2: 
                #퍼즐 섞음
                ne = nx * 2 + ny
                puzzle_list = list(puzzle) 
                #순서 바꾸기
                puzzle_list[e], puzzle_list[ne] = puzzle_list[ne], puzzle_list[e]
                
                n_puzzle = ''.join(puzzle_list) 
                
                #방문 안했으면
                if visited.get(n_puzzle, 0) == 0:
                    visited[n_puzzle] = cnt 
                    q.append(n_puzzle)
    return -1
                    
print(bfs())