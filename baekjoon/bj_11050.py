n, k = map(int, input().split())
sum=0
def fac(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fac(n-1)
    
print(fac(n) // (fac(k)*fac(n-k)))