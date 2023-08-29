import sys
input = sys.stdin.readline
from collections import defaultdict
dic =defaultdict(int)
n = int(input())
for i in range(0, n+1):
    i = str(i)
    for j in i:
        dic[j]+=1
print(dic)