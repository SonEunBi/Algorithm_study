import sys
input = sys.stdin.readline

n = int(input())
t=[]
p=[]
dp = [0 for _ in range(n+1)] #금액 더할거임

for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    
for i in range(n-1, -1, -1):
    if t[i]+i > n: #퇴사후까지 상담하게 생겼으면 패스
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[t[i]+i] + p[i])

print(dp[0])
