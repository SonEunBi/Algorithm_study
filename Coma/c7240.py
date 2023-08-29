import sys
input = sys.stdin.readline

n = int(input())
graph =[[0]*(5) for i in range(5)]
for i in range(n):
    idx = i+1
    a,b,w,h = map(int, input().split())
    if a > w and b>h: #a,b가 더 클 때
        a,b = w,h
    for i in range(a, w):
        for j in range(b,h):
            graph[i][j] =idx
for i in range(5):
    print(*graph[i])        