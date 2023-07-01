import sys
read = sys.stdin.readline

a, b, c = map(int, read().split())
price, sell=0,0
i, break_point =0,0
while 1:
    price = a + b*i
    sell = c*i
    if b>= c:
        break_point='-1'
        break
    elif price <sell :
        break_point = i
        break
    i+=1
print(break_point)
    
