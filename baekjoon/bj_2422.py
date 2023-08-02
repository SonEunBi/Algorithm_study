import sys
input = sys.stdin.readline
from itertools import permutations

n, m = map(int, input().split())
num = [1 for i in range(1, n+1)]
graph=[[]*(n+1) for _ in range(1, n+1)]
s= set()
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
