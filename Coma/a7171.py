import sys

a,b,c = map(int, input().split())
if a+b+c == 180 and min(a,b,c) >0:
    print('P')
else:
    print('F')