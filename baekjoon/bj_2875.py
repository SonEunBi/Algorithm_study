import sys
input = sys.stdin.readline
ans =0
n, m, k = map(int, input().split())
#m의 수가 출전할 수 있는 최대 팀 수
while n>=2 and m>=1 and n+m >= k+3:
    n-=2
    m-=1
    ans += 1
print(ans)