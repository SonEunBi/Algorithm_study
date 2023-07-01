import sys
read = sys.stdin.readline

n, m = map(int, read().split())
bucket = [i for i in range(1, n+1)]

for i in range(m): #교환 횟수
    start, end = map(int, read().split())
    tmp = 0
    bucket[start-1], bucket[end-1] = bucket[end-1], bucket[start-1]
    
for i in range(len(bucket)):
    print(bucket[i], end=' ')