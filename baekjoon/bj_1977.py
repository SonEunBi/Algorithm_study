import sys
input = sys.stdin.readline

a=int(input())
b= int(input())
ans =[]

for i in range(a,b+1):
    root = i**0.5
    print(root)
    if i == root**2:
        print(i)
        ans.append(i)

if ans:
    print(sum(ans))
    print(min(ans))
else:
    print(-1)