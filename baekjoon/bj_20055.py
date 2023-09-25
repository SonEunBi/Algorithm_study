import sys
input = sys.stdin.readline

n, k = map(int, input().split())
belt =list(map(int, input().split()))
# tmp= map(int, input().split())
# for idx, power in enumerate(tmp):
#     belt.append([idx, power, 0])
    
def solution(n, belt):
    step =1 #처음 수행은 1번째 단계
    robot = [False for _ in range(n)]
    while 1: #-1 로 하면 integer로 인식, int + list로 오류 뜨기 때문에 [-1:]로 처리해줘야 함
        belt = belt[-1:] + belt[:-1]
        robot = robot[-1:] + robot[:-1]
        
        if robot[n-1]:
            robot[n-1]=False
            
        for now in range(n-1,-1,-1): #매번 검사해야 하는 것들
            #뒤에서부터 검사함
            nxtidx = (now+1)%len(robot)
            
            if robot[now] and not robot[nxtidx] and belt[nxtidx] >0:
                robot[now] =False
                robot[nxtidx] =True
                belt[nxtidx] -=1
                if robot[n-1]:
                    robot[n-1] = False

        if belt[0] >0:
            belt[0] -= 1
            robot[0] =True
        
        total =0
        for p in belt:
            if p <1:
                total +=1
        if total >= k:
            break

        step+=1
    return step
            

    
print(solution(n, belt))
        
        