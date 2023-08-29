import sys
from collections import defaultdict

a, b = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

maxi = arr[0]
dic = defaultdict(int)

for i in range(len(arr)):
    if arr[i] in dic:
        dic[arr[i]]+=1
    else:
        dic[arr[i]] =1

s = dic[arr[0]]

for i in range(1,len(dic)):
    if arr[i] in dic:
        s += dic[arr[i]]
        if s == b:
            print(arr[i-1])
            print(arr)
            break
    
