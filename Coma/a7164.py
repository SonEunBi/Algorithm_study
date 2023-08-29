import sys

a, b,n = map(int, input().split())
for i in range(a, b*n-a+2, b):
    ans = i

print(ans)