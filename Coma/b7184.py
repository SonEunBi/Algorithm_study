import sys

a, b= map(int, input().split())
nlist = list(map(int, input().split())) +[0]
flag,idx =0,0
for i in range(len(nlist)):
    if nlist[i] == b:
        flag = 1
        idx = i+1
if flag == 1:
    print(idx)
elif flag ==0:
    print('-1')
