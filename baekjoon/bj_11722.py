import sys
input = sys.stdin.readline

n= int(input())
arr = list(map(int, input().split()))
dp = [1 for i in range(n)]

for i in range(n):
    for prev in range(0, i):
        if arr[prev] > arr[i]:
            dp[i] = max(dp[prev]+1, dp[i])
print(max(dp))