import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

dp =[1 for i in range(len(lst))]
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] < lst[j]: #j가 더 크면
            dp[j] = max(dp[j], dp[i]+1)

print(max(dp))