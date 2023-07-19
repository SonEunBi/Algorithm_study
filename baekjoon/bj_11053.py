import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
dp = [1 for i in range(n)]

for now in range(n): #현재 비교할 수
    for prev in range(now): #0부터 비교할 수의 직전까지
        if lst[now] > lst[prev]:
            dp[now] = max(dp[now], dp[prev]+1)
    print(dp)
            
print(max(dp))