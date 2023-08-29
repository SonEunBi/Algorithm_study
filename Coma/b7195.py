import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
num =0
lst.sort(reverse=True)
if max(lst) == 0: #0이 제일 큰 수일 때
    print('0')
else:
    if lst[-1] == 0:
        del lst[-1]
        num = ''.join(map(str, lst)) #str
        if int(num) %3 ==0 and num[-1]=='0': #3의 배수
            print(num+'0')
        else:
            print('-1')
    else:
        print('-1')