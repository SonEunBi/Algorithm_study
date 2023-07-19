import sys
input = sys.stdin.readline

n = int(input())
stair=[0]*(301)
dp =[0]*(301)
for i in range(1, n+1):
    stair[i] = int(input())

dp[1] = stair[1]
dp[2] = dp[1] + stair[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])
    
print(dp[n])
