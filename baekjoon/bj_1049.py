import sys
input = sys.stdin.readline

result =0
remain =0
n, m = map(int, input().split(' '))
minpack = 1001
minsing = 1001
for i in range(m):
    p, s = map(int, input().split(' '))
    minpack = min(minpack, p)
    minsing = min(minsing, s)
    
if minpack > minsing*6:
    result += minsing*n
else: #패키지가 더 저렴하면
    result += minpack*(n//6)
    if (n%6) * minsing < minpack:
        result += n%6*minsing
    else:
        result += minpack
print(result)