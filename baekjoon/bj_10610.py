import sys
from itertools import permutations
input = sys.stdin.readline

n = list(input().strip('\n'))
n.sort(reverse=True)
ans =0
res =[]
if '0' in n:
    n = list(map(int, n))
    if sum(n) %3==0:
        print(''.join(map(str, n)))
    else:
        print('-1')
else: 
    print('-1')
    