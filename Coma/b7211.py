import sys
input = sys.stdin.readline

a, b = map(int,input().split())
fib = [0,1]
idx =1
i=1
prev, pprev = 1, 0

while idx <= b:
    idx += i
    fib.append(i*i)
    if idx == b:
        print(sum(fib[a:b+1]))
        break
    elif idx > b:
        print(sum(fib[a:b+1])- i*(idx-b))
        break
    pprev, prev = prev, i
    i = prev + pprev
    