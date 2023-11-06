import sys
input = sys.stdin.readline

a, b = map(int, input().split())
tmp = ''
ans = ''
s = input()

for i in range(len(s)):
    ans += s[i]*b
print(ans)