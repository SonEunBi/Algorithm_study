import sys
input = sys.stdin.readline

scr, bsk = map(int, input().split())
n = int(input())
arr=[]
l = 1
r = bsk
for i in range(n):
    fall = int(input())
    if r < fall: #오른쪽에 떨어졌을 때
        arr.append(abs(fall-r))
        r= fall
        l= r-bsk+1
    elif l > fall : #왼쪽에 떨어졌을 떄 
        arr.append(abs(fall-l))
        l = fall      
        r = l+bsk-1
print(sum(arr))