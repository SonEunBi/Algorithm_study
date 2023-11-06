import sys
input = sys.stdin.readline
import math
#최대공약수
a= map(int, input())
lst= list(map(int, input().split()))
lst.sort()
if lst[0]==1:
    a_i = 1
else:
    a_i = math.gcd(lst[0], lst[1])
print(a_i)
