import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temp = list(map(int, input().split()))

window = sum(temp[:k])
ans = window

for i in range(k, n):
    window += temp[i] - temp[i-k]
    if window > ans:
        ans = window
print(ans)