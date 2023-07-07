import sys
input = sys.stdin.readline

n, s = map(int, input().split()) #목표값 s
n_list= list(map(int, input().split()))
cnt =0
def dfs(i, sum):
    global cnt
    if i >= n:
        return
    sum += n_list[i]
    if sum == s:
        cnt += 1
        
    dfs(i+1, sum)
    dfs(i+1, sum - n_list[i])
dfs(0,0)
print(cnt)
    