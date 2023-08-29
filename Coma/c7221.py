import sys
input = sys.stdin.readline

n = int(input())
coin = [list(input()) for _ in range(n)]
ans =0
for k in range(1<<n):
    tmp = [coin[i] for i in range(n)]
    for i in range(n):
        if k & (1<<i):
            for j in range(n):
                if tmp[i][j] == 'W':
                    tmp[i][j] = 'B'
                else:
                    tmp[i][j] = 'W'
                    
    s =0
    for i in range(n):
        cnt =0
        for j in range(n):
               if tmp[j][i] == 'B':
                    cnt +=1 
        s += min(cnt, n-cnt)
    ans = min(n*n+1, s)
print(ans)