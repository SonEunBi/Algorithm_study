import sys
input = sys.stdin.readline

a,b = map(int,input().split())
cnt=1
while a!=b:
    tmp =b
    if b%10 ==1:
        b//=10
        cnt+=1
    elif b%2==0:
        b//=2
        cnt+=1
    if tmp == b:
        cnt = -1
        break
print(cnt)