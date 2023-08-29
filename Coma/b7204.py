import sys
input = sys.stdin.readline
from math import trunc
meter = int(input())
n = int(input())
start =[]
end = []
for i in range(n):
    carnum, stime = input().split()
    start.append((carnum, stime))
start = sorted(start, key = lambda x: (x[0]))

for i in range(n):
    carnum, etime = input().split()
    end.append((carnum, etime))
end = sorted(end, key = lambda x: (x[0]))

for i in range(n):
    hh1, mm1, ss1 = map(int, end[i][1].split(':'))
    hh2, mm2, ss2 = map(int, start[i][1].split(':'))
    #hour가 기준
    
    diff = (hh2-hh1) + (mm2-mm1)*(1/60) + (ss2-ss1)*(1/3600)
    
    print(start[i][0], abs(trunc(meter/diff)))