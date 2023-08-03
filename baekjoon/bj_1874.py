import sys
input = sys.stdin.readline

n =int(input())
stack =[]
now =1
ans = []
flag =0
for i in range(1, n+1):
    dst = int(input().rstrip())
    
    while now <= dst:
        stack.append(now)
        now+=1
        ans.append('+')
    if stack[-1] == dst:
        stack.pop()
        ans.append('-')
    else:
        flag =1
        break    
    
if flag ==0:
    print('\n'.join(ans))
else:
    print('NO')