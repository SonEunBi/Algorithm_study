def solution(today, terms, privacies):
    answer = []
    #1 ≤ DD ≤ 28
    
    def cmp(ay, am, ad, today):
        ty, tm, td = today.split('.')
        if int(ty) < int(ay):
            return 1
        elif int(ty) == int(ay):
            if int(tm) < int(am):
                return 1
            elif int(tm) == int(am):
                if int(td) <= int(ad):
                    return 1
                else: 
                    return 0
            
    rule = dict()
    stand = dict()
    
    for i in range(len(terms)):
        r, d = str(terms[i]).split(' ')
        rule[r] =d
    
    for j in range(len(privacies)):
        flag =0
        info,r = str(privacies[j]).split(' ')
        y,m,d = map(int, info.split('.'))
        ay = y
        am = m + int(rule[r])
        while am > 12:
            am -= 12
            ay = y + 1
        
        if d ==0:
            ad = 28
            am -= 1
            if am == 0:
                am =12
                ay = int(y) -1
        else:
            ad = d - 1
            
        flag = cmp(ay,am,ad,today)
        if not flag ==1:
            answer.append(j+1)
    
    return answer