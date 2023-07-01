import sys
read = sys.stdin.readline
from itertools import combinations

L = int(read())
s = list(map(int, read().split()))
num = int(read())
s.sort()
ans, start=0,0
end=0
for i in range(L):
    if s[i] <= num & s[i+1] >= num:
        end = s[i+1]
        start = s[i]
        break
end = num - start
start = end - num

ans = end * start -1
print(ans)