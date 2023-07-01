import sys
input = sys.stdin.readline

n= int(input())
arr = list(map(int, input().split()))
dp = [1 for i in range(n)]
for i in cp_arr:
    for j in range(len(arr)):
        if i == arr[j]:
            