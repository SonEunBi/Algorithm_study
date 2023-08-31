import sys
from collections import defaultdict

a, b = map(int, input().split())
arr = list(map(int, input().split()))
arr_copy = sorted(arr, reverse=True)

rank = defaultdict(int)

#등수
for i in range(len(arr_copy)):
    if arr_copy[i] in rank:
        rank[arr_copy[i]]+=1
    else:
        rank[arr_copy[i]] =1

# for i in range(1,len(rank)):
#     if s >= b:
#         break
#     elif arr_copy[i] in rank:
#         s += rank[arr[i]]
#         if s == b:
#             print(arr[i-1])
#             print(arr)
#             break
ans =0    
cutline = max(arr)
for key, value in rank.items():  
    ans += value
    if ans == b:
        print(key)
        break 
    elif ans > b+1:
        print(min(arr)-1)
    for i in range(len(arr)):
        if arr[i] == key: #해당 순서일 때
            if i ==0 or i == a-1: #맨 끝에 있는 얘면
                ans +=1 #1명 추가
            else:
                ans +=2 #양옆 두 명 추가

for key, value in rank.items():
    ans += value
    if ans == b:
        print(key)
        break
    elif ans > b and key == max(arr):
        print(min(arr)-1)
    else:
        if i ==0 or i == a-1: #맨 끝에 있는 얘면
                ans +=1 #1명 추가
            else:
                ans +=2 #양옆 두 명 추가
        
    