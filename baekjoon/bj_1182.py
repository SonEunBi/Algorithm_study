import sys
input = sys.stdin.readline
from itertools import permutations

n, s = map(int, input().split()) #목표값 s
num= list(map(int, input().split()))
a = set()
cnt  =0
for i in range(n):
    for per in permutations(num,i):
        ans = sum(per)
        if ans == a:
            a.add(per)
            print(a)
print(len(a))