import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ice = [0 for i in range(1000001)]
last =0
for i in range(n):
    a, b = map(int, input().split())
    ice[b] = a
    last = max(last, b)

window_size = 2*k+1
window = sum(ice[:window_size]) # 오른쪽을 움직인다고 생각하기
ans = window 

for i in range(window_size, last+1):
    window += ice[i] - ice[i-window_size]
    ans = max(ans, window)
print(ans)

