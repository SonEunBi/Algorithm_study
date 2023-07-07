from collections import deque
import sys
read = sys.stdin.readline

n, k = map(int, read().split())

q = deque([])
ans = []
for i in range(n):
    q.append(i+1)

for _ in range(n):
    for _ in range(k-1):
        num = q.popleft()
        q.append(num)
    num = q.popleft()
    ans.append(num)
print("<{}>".format(str(ans)[1:-1]))
        