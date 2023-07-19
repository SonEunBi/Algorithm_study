import sys
import math
input = sys.stdin.readline

w,h,n,m = map(int, input().split()) #세로 n, 가로 m

ans1 = math.ceil(w/(n+1))
ans2 = math.ceil(h/(m+1))
print(ans1*ans2)