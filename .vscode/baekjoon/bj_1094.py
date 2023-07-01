#print(bin(int(input())).count('1'))

n = int(input())
bar = [64,32,16,8,4,2,1]
ans =0
now =0
while n:
    if now <= n:
        