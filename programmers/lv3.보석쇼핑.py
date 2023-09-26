from collections import Counter

def solution(gems):
    answer = []
    end,start =0,0
    l = len(set(gems)) #진짜배기들
    gemcnt =Counter()
    
    while end < len(gems):
        while end < len(gems) and len(gemcnt) != l:
            
            if gems[end] in gemcnt:
                gemcnt[gems[end]] +=1
            else: 
                gemcnt[gems[end]] =1
            end +=1
        
        while start < len(gems) and len(gemcnt) == l:
            gemcnt[gems[start]] -=1
            if gemcnt[gems[start]] ==0:
                gemcnt.pop(gems[start])
            start +=1
            
        answer.append((end-start, start, end)) #짧은 거리를 구해야 하니까!!
    answer.sort()
                 
    return answer[0][1], answer[0][2]