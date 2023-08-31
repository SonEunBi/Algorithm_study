n ,m = map(int, input().split())
dp = [0,0,0,12]
if n > 3 :
    for i in range(4,n+1):
        dp.append(dp[i-1]*i)
    print(dp[n]%1000000007)
else :
    print(dp[n])