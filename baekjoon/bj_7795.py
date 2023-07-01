import sys
read = sys.stdin.readline
from itertools import product
import bisect

n = int(read().rstrip())
for i in range(n):
    anum, bnum = map(int, read().split())
    a= sorted(list(map(int, read().split())))
    b=  sorted(list(map(int, read().split())))
    cnt =0
    for j in a:
        cnt += bisect.bisect(b, j-1)
    print(cnt)
    
