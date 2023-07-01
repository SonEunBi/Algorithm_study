import sys
read = sys.stdin.readline

n,m = map(int, read().split())
bucket = [0]*(n)
for i in range(m):
    start, end, num = map(int, read().split())
    for j in range(start, end+1, 1):
        bucket[j-1] = num

for i in range(n):
    print(bucket[i], end=' ')