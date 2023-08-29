import sys
input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[0]*(v+1) for i in range(v+1)]
c1 = []
c2 = []
for i in range(e):
    a, b = map(int, input().split())
    graph[a][b] =1
    graph[b][a] =1
    
    c1.append(a)
    c2.append(b)
print(c1, c2)


    