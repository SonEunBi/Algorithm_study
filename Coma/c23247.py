import sys
input = sys.stdin.readline

n, m = map(int, input().split())
rect = [list(map(int, input().rstrip('\n').split())) for _ in range(n)]
res = [[0]*(m+1) for _ in range(n+1)]

ans =0
for i in range(n):
    for j in range(m):
        if i ==0 and j==0: #배열이 시작하면
            res[i+1][j+1] = rect[i][j] #초기값 저장
        elif i==0: #이전 열은 0이니까 누적합 저장
            res[i+1][j+1] = rect[i][j] + res[i+1][j]
        elif j ==0: #이전 행은 0이니까 누적합 저장
            res[i+1][j+1] = rect[i][j]+res[i][j+1]
        else: #현재 위치 + 바로 위 누적합 + 왼쪽 누적합 더하고 중복값 빼주기
            res[i+1][j+1] = rect[i][j] + res[i+1][j]+res[i][j+1] - res[i][j]
            
cnt =0
for i in range(1, n+1): #왼쪽 위(i,j)
    for j in range(1, m+1):
        for k in range(i, n+1): #오른쪽 아래(k,t)
            for t in range(j, m+1):
                ans = res[k][t] - res[k][j-1] - res[i-1][t] + res[i-1][k-1]
                if ans >=10:
                    if ans == 10:
                        cnt +=1 
                    break
print(cnt)