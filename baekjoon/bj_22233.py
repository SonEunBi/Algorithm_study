import sys
input = sys.stdin.readline

n,m = map(int, input().split())

memo={}
for i in range(n):
    a= input().strip()
    memo[a] = ""
    
for _ in range(m):
    b = input().strip().split(',')
    for i in range(len(b)):
        if b[i] in memo:
            del memo[b[i]]
    print(len(memo))