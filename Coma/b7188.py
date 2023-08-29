import sys
from math import ceil, log

n = int(input())
nums = list(map(int, input().split()))
tree = [0]*(n*4)

def segment_tree(start, end, now):
    if start == end:
        tree[now] = nums[start]
        return tree[now]
    
    mid = (start+end)//2
    tree[now] = segment_tree(start, mid, now*2) +segment_tree(mid+1, end, now*2 +1)
    return tree[now]

def update(start, end, now, idx, diff):
    if end < idx or idx < start:
        return 0
    tree[now]+= diff
    
    if start != end:
        mid = (start+end)//2
        update(start, mid,now*2, idx, diff)
        update()
        
segment_tree(1, n+1, 1)
print(update(1, n+1, 1, 1, n ))