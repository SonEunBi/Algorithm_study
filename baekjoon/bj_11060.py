import sys
input = sys.stdin.readline

n = int(input())
board=list(map(int, input().split()))
dp=[n]*n
dp[0]=0
for cur in range(0, n-1):
    for nxt in range(1, board[cur]+1):
        if cur+nxt < n:
            dp[cur + nxt] = min(dp[cur+ nxt],dp[cur]+1)
            print(dp)
            
if dp[n-1] == n+1:
    print('-1')
else:
    print(dp[n-1])