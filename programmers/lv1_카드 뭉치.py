from collections import deque
def solution(cards1, cards2, goal):
    answer = 'Yes'
    sentence = []
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    
    for word in goal:
        if len(cards1) !=0 and cards1[0] == word:
            cards1.popleft()
        elif len(cards2) != 0 and cards2[0] == word:
            cards2.popleft()
        else:
            answer='No'     
            break
            
    return answer