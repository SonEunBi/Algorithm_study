import sys
input = input
boat, S, R = map(int, input().split())
boat = [1 for _ in range(boat)]
df = list(map(int, input().split()))
good = list(map(int, input().split()))
for i in df:
    boat[i-1] -= 1
for i in good :
    boat[i-1] += 1
    
for i in range(len(boat)) :
    if boat[i] < 2 :
        continue
    if i > 0 and boat[i-1] < 1 :
        boat[i] -= 1
        boat[i-1] += 1
        continue
    if i + 1 < len(boat) and boat[i+1] < 1 :
        boat[i] -= 1
        boat[i+1] += 1

print(boat.count(0))