from itertools import permutations
 
def solution(numbers):
    answer = 0
    arr =[]
    s= set()
    cnt =0
    chk = True
    
    for i in range(1, len(numbers)+1):
        tmp = list(map(''.join, permutations(numbers, i)))
        for j in tmp:
            s.add(int(j))
    
    for i in s: #에라토스테네스의 체
        i = int(i)
        chk = True
        if i >= 2:
            for j in range(2, int(i**0.5)+1):
                if i%j ==0:
                    chk = False
            if chk:
                cnt+=1
    
    return cnt