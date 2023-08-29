import sys
input = sys.stdin.readline

n, m = map(int, input().split())
money = sorted([int(input().rstrip('\n')) for i in range(n)])
dp =[10001]*(m+1)
dp[0]= 0

for i in range(1,m+1):
    for j in money:
        if i-j < 0:
            break
        else:
            dp[i] = min(dp[i-j]+1, dp[i])
print(-1 if dp[m]==10001 else dp[m])