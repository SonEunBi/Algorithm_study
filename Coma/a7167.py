import sys

a = input() 
pw = []
flag =0
for i in a:
    if not i.isalpha():
        flag =1
    pw.append(i)
    
if len(pw) <= 20 and flag ==0:
    print('P')
else:
    print('I')