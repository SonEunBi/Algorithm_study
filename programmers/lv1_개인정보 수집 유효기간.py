def convert(date):
    y,m,d = map(int, date.split('.'))
    return y*12*28 + m*28 + d
    
def solution(today, terms, privacies):
    answer = []
    rule = dict()
    today = convert(today)
    
    for term in terms:
        a, b = term.split(' ')
        rule[a] = int(b)*28
    i=1
    for pri in privacies:
        date, r = pri.split()
        standard = convert(date) + rule[r]
        if standard <= today:
            answer.append(i)
        i+=1
    
    return answer