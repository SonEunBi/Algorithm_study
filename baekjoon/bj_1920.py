import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
m = int(input())
num = list(map(int,input().split()))
answer = []
i =0

start =0
end =0
while num:
    mid = lst[n//2+1]
    if mid == num[i]:
        answer.append(1)
        continue
    else:
        if mid > num[i]:
            end = mid-1
            mid = (start + end)/2
        elif mid <num[i]:
            start = mid+1
            mid = (start + end)/2

print(answer)
    