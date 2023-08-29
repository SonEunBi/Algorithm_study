import sys
input = sys.stdin.readline

n = int(input())
perma = [1, 3,5,17,257,65537]
multi = []
for i in range(len(perma)):
    for j in range(i, len(perma)):
        multi.append(perma[i]*perma[j])

if n in perma:
    print('YES')
else:
    
    if (n&(n-1))==0: #2의 배수이면
        print('YES')
    else:
        print('NO')