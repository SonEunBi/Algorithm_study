# -*- coding: utf-8 -*-
import sys
from itertools import permutations
arr=list(map(int,input().split()))
for per in permutations(arr,2):
    print(per)