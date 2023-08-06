import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque()
    q.append((hx, hy))
    while q:
        x, y = q.popleft()
        if abs(x - fx) + abs(y - fy) <= 1000:
            print('happy')
            return
        
        for i in range(n):
            if not visited[i]:
                nx, ny = conv[i] #편의점만 집중적으로 보기
                if abs(x-nx) + abs(y-ny) <=1000:
                    visited[i] =1
                    q.append((nx, ny))
    print('sad')
    return

t= int(input())
for _ in range(t):
    conv = []
    n = int(input())
    hx, hy = map(int, input().split())
    for _ in range(n):
        cx, cy = map(int, input().split())
        conv.append((cx, cy))
    fx, fy = map(int, input().split())
    visited = [0 for _ in range(n+1)]    
    bfs()
                
                
    


                
            
    