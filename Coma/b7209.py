import sys
input = sys.stdin.readline

a, b = map(int, input().split())
digit  = int(input())
n =1
while a*n <= b:
    n+=1
    if a*n == b:
        print(n)
        break
    elif n <= a-1