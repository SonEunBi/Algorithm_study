import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
belt =deque(list(map(int, input().split())))
robot = deque([0 for _ in range(n)])

step =0
while belt.count(0) < k:
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0 #내리는 위치
    if sum(robot) >0:
        for now in range(n-1, -1, -1): #이미 -1은 검사했으니까
            nxtidx = (now+1)%n
            if robot[now] and robot[nxtidx] == 0 and belt[nxtidx] >0:
                robot[now] = 0
                robot[nxtidx] =1
                belt[nxtidx] -=1
            robot[-1] =0
    if belt[0] >0:
        robot[0] =1
        belt[0] -=1
    step +=1
    
print(step)
    
    