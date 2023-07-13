import sys
input = sys.stdin.readline

n =int(input())
answer =[]
stack =[]
now =1
flag =0
for i in range(n):
    x = int(input())
    while now <= x:
        stack.append(now)
        now+=1
        answer.append('+')
        
    if stack[-1] == now:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        flag =1
        break
if flag ==0:
    print('\n'.join(answer))