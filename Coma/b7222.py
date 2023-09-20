import sys
input = sys.stdin.readline

n = int(input())
ans =0
dp = [0]*(n+1)
dp[0] = 1
dp[1] =0
dp[2] =3
dp[3] =0 
    
for i in range(4, n+1):
    dp[i] = 2*dp[i-1] + dp[i-2]
    
ans = dp[n]
print(ans)