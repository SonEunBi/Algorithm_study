import sys
input = sys.stdin.readline

pw = input()
ans = []
for i in pw:
    ans.append(i)
    if i == 'c' :
        break
        
print(''.join(ans))