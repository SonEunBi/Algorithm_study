# -*- coding: utf-8 -*-
import sys

n = int(input())
l = list(map(int, input().split()))
flag =0
idx =0
for i in range(len(l)):
    if l[i] <= 160:
        flag =1
        idx = i+1
        break

if flag == 0:
    print('P')
else:
    print('I', l[idx-1])