import sys
input = sys.stdin.readline

n = int(input())
rst = list(input().rstrip())
lst=[]

for i in range(n):
    cmd= list(input().split())
    if cmd[0] == 'P':
        rst.append(cmd[1])
        
    elif cmd[0]=='L':
        if rst:
            lst.append(rst.pop()) 
        
    elif cmd[0]=='D':
        rst.append(lst.pop())
        
    elif cmd[0] =='B':
        if rst:
            rst.pop()

print(lst, rst)
print(''.join(map(str, rst)))