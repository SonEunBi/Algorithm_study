import sys
input = sys.stdin.readline

n, m = map(int, input().split())
day = list(map(int, input().split()))

window = sum(day[:m])
cnt =0
ans = window
for i in range(m, n):
    window += day[i] - day[i-m]
    if window > ans:
        ans = window
print(ans)
