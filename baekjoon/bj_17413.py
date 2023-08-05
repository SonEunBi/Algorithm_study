import sys
input = sys.stdin.readline

s = list(input().rstrip() + ' ')
stack =[]
ans = ''
for i in s:
    if i == '<':
        while stack:
            stack.reverse()
            
        ans += i
        while i != '>':
            ans += i
        ans += i
        
    elif i == ' ':
        while stack:
            ans += stack.pop()
        ans += ' '

    else:
        stack.append(i)
print(ans)