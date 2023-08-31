import sys
input = sys.stdin.readline

def pretty(num):
    num_s = str(num)
    n = len(num_s)
    
    for i in range(1, n):
        prefix = int(num_s[:i])
        suffix = int(num_s[i:])
        
        if str(prefix) in num_s and num % prefix == 0:
            return True
    
    return False

num = int(input())

if pretty(num):
    print("YES")
else:
    print("NO")