a = ' ' + input().rstrip()
b = ' ' +input().rstrip()

dp =[[0]*(len(a)) for _ in range(len(b))]
for i in range(1, len(b)):
    for j in range(1, len(a)):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] +1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            
print()