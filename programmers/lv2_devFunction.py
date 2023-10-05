def solution(progresses, speeds):
    answer = []
    rest = []
    day = []
    cnt=0
    for i in progresses:
        rest.append(100 - i)
    
    for i in range(len(rest)):
        if rest[i]%speeds[i] ==0:
            day.append(rest[i]//speeds[i])
        else:
            day.append(rest[i]//speeds[i]+1)
            
    for d in range(len(day)):    
        cnt +=1
        if day[d] < day[d+1]:
            answer.append(cnt)
            cnt =0
        
    return answer