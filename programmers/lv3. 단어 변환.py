from collections import deque
 
def solution(begin, target, words):
    if target not in words:
        return 0
    
    q = deque()
    q.append([begin, 0])
 
    while q:
        tmp, cnt =q.popleft()
        
        if tmp ==target: #같으면 cnt 반환
            return cnt
        
        for i in range(len(words)): #word리스트 기준으로 돌리는데
            chk = 0 #검사 변수 리셋해주고
            word = words[i] #처음 단어를 word 변수에 넣어줌
            
            for j in range(len(tmp)):  #현재 저장된 단어(바로 직전에 검사한 단어의 길이만큼)
                if tmp[j] != word[j]: #단어 검사
                    chk +=1 #단어 틀리면 1씩 증가
            if chk == 1: #만약 1개만 틀렸으면
                q.append([word, cnt+1]) #[단어, cnt+1] 이 자체를 q에 넣어줌
    return 0 #위에서 cnt로 반환하니까 상관없음