import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lv = [input().split() for _ in range(n)]

def bisect(i):
    left =0
    right = len(lv)-1
    result =0
    while left <= right:
        mid= (left+right)//2
        if i <= int(lv[mid][1]): #중간 값보다 해당 수가 작을 때
            right = mid-1
            result = mid
        else: #수가 작을 떄
            left = mid+1
    return lv[result][0]

for _ in range(m):
    power = int(input())
    print(bisect(power))