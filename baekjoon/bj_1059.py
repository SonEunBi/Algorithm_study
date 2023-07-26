import sys
read = sys.stdin.readline

L = int(read())
s = list(map(int, read().split()))
num = int(read())
s.sort()
start=0
end=0
for i in range(L-1):
    if s[i] <= num <= s[i+1]:
        end = s[i+1]
        start = s[i]
        break
end = end-1-num
start = num-start+1

def fac(n):
    if n == 1 or n==0:
        return 1
    else: 
        return n*fac(n-1)
    
print(fac(end-start))