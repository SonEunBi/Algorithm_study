import sys
input = sys.stdin.readline

a, b,c,d = input().split()
a= int(a)
flag =0 #이미 정해진 결과인지 아닌지
if a == 0: #0년차
    flag =1
    print(a)
else:
    if d == 'Private': #병
        if c == 'Y': #동원 지정
            print('28')
        else: #동원 미지정
            if a in (5,6): #5,6년차
                print('20')
            else:
                if b == 'ROKAF':
                    print('28')
                else:
                    print('32')
                
    else: #간부
        print('28')
        
    
    