import sys
input = sys.stdin.readline

n  = int(input())
dp = [0]*(n+1) #계산한 결과값을 더해주는 것이 아니라, 몇 번 계산했는지를 더해줄 것임
for i in range(2, n+1): #5
    dp[i] = dp[i-1]+1 #한 번 더 계산했다는 뜻
    if i%3==0: 
        dp[i]= min(dp[i], dp[i//3]+1)#만약 i가 9라면 이미 i//3인 3에는 그 때의 계산 결과값이 있을 것임. 그걸 불러오는 것이다.
    if i%2 ==0:
        dp[i] = min(dp[i], dp[i//2]+1) #지금의 계산 횟수가 작느냐, i//2를 했을 때에서 +1(지금것까지) 했을 때가 작은지의 차이
print(dp[n])