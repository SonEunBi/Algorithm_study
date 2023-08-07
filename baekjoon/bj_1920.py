import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
num = list(map(int, input().split()))

def bisect(num):
    flag =0
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == num:
            print('1')
            flag =1
            break 
        elif arr[mid] > num:
            end = mid -1
        elif arr[mid] < num:
            start = mid +1
    if flag ==0 :
        print('0')
        
        
for i in num:
    bisect(i)
    