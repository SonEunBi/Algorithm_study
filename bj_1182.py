import sys
read = sys.stdin.readline

n, s = map(int, read().split())
arr = list(map(int, read().split()))
cnt =0 

def back_tracking(idx, sum):
    global cnt
    if idx == n: #현재 수가 몇 번째인지, n번째면
        if sum == s: #합계가 sum이면
            cnt +=1
        return #함수를 빠져나감
   
    back_tracking(idx+1, sum) #시작하는 숫자를 다르게 할거임
    back_tracking(idx+1, sum+arr[idx])
        
back_tracking(0,0)
print(cnt)
print(cnt-1 if s==0 else cnt)


"""
import sys
from itertools import combinations

IN = sys.stdin.readline().split()
while IN[0] != '0':
    cm = combinations(IN[1:], 6)
    for c in cm:
        print(' '.join(c))
    print()
    IN = sys.stdin.readline().split()
    """