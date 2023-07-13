import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c,d = map(int, input().split())

def gcd(b,d ):
    if b < d:
        b,d = d,b
    if d ==0:
        return b
    else:
        return gcd(d, b%d)

top =a*d+ c*b
bottom = b*d 
gcd1 = gcd(top, bottom)
print(top//gcd1,bottom//gcd1)