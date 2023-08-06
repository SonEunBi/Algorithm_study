import sys
input = sys.stdin.readline

city = int(input())
road =[0]+ list(map(int, input().split()))
price = [0]+list(map(int, input().split()))
std = price[1]
ans = 0
for i in range(1, city):
    if price[i] < std:
        std = price[i]
        
    ans += road[i]*std
print(ans)