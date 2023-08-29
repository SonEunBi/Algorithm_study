import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
dice1 = [1,2,3,4,5,6]
dice2= [1,2,3,4,5,6]

for i in dice1:
    for j in dice2:
        if i +j == n:
            print(i, ' ',j)
        
