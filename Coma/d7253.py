import sys
input = sys.stdin.readline
from math import gcd 

n = int(input())
lst = sorted([int(input().rstrip('\n')) for _ in range(n)])
num=[]
ans = set()

for i in range(1, n): #숫자간의 차이 구하고
    num.append(lst[i]- lst[i-1])
gcd_num = num[0]

for i in range(1, n-1):
    gcd_num = gcd(num[i], gcd_num)

for i in range(1, int(pow(gcd_num, 1/2)) +1):
    if gcd_num % i == 0:
        ans.add(i)
        ans.add(gcd_num // i)
print(' '.join(map(str, sorted(ans))))