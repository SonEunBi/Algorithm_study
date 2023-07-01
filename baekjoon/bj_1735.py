import sys
read = sys.stdin.readline

def gcd(x, y):
    while y >0 :
        x, y = y, x%y
    return x

a,b = map(int, read().split())
c, d = map(int, read().split())
n = 0
ans = a*