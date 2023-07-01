import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ans =0
castle = []
for i in range(n):
    castle.append(input())
    
for i in range(n):
    if "X" not in castle[i]:
        ans += 1

for j in range(m):
    