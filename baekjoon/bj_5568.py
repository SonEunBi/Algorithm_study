from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
k =int(input())
nlist =[]
for i in range(n):
    nlist.append(input().rstrip())

s = set()
for per in permutations(nlist, k):
    s.add(''.join(map(str, per)))


print(len(s))