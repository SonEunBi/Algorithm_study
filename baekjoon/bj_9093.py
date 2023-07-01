import sys
read= sys.stdin.readline

ans =[]
t = int(input())
strlst = []
for i in range(t):
    ans.clear()
    strlst = list(map(str, read().split()))
    for j in strlst:
        ans.append(j[::-1])
    print(' '.join(ans))
    