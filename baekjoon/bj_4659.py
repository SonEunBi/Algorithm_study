import sys
input = sys.stdin.readline

vowel = ['a', 'e', 'i', 'o','u']

while True:
    cnt =0
    vchk =0
    cchk =0
    prev =''
    psw = input()
    if psw == 'end':
        break 
    for i in psw:
        if cchk ==3 or vchk ==3: #2번 문제 끝
            print('<',psw, '> is acceptable.')
            continue
        if i in vowel: #1번
            if prev == i:
                if (prev == 'e' and i == 'e') or (prev == 'o' and i =='o'):
                    vchk-=1                
            vchk+=1
            cchk=0
        else:
            vchk =0
            cchk +=1
        prev = i

        
        if vchk ==0:
            print('<'+psw +'> is acceptable.')
            continue
        
    
        
            
        