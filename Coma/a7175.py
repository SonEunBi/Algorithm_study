import sys
input = sys.stdin.readline

n = int(input())
new_dic=[]
dic = dict()
a, b =0,0
for i in range(n):
    a, b = input().split()
    b = int(b)
    dic[a] = b
print(dic)
new_dic = sorted(dic.items(), key= lambda x : (x[1] , x[0]), reverse=True)[:3]
print(dic)
for i in range(3):
    print(dic[0])