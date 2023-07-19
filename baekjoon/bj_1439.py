import sys
input = sys.stdin.readline

n = list(map(int, input().strip()))
zero = n.count(0)
one = n.count(1)
flag =1

for i in range(len(n)-1):
    if n[i] != n[i+1]:
        flag+=1
print(flag//2)