import sys
input = sys.stdin.readline

n = int(input())
req = [0] + list(map(int, input().split()))
req.sort()
maxi = int(input())
temp = []
if sum(req) <= maxi: #괜찮을 때
    print(max(req))
elif min(req)*n > maxi: #원숭이들이 터무니없는 식량을 부를 때
    print(maxi // n)
else: 
    for i in range(1, n):
        tmp=0
        temp=[]
        tmp += sum(req[:i+1]) #i까지 저장하고
        temp.append(req[:i+1])
        print(temp)
        tmp += (n-i)*req[i+1] #현재 최소 값으로 식량 때우면
        temp.append(req[i+1:])
        print(temp)
        if tmp >= maxi:
            print(req[i+1])
            break
        