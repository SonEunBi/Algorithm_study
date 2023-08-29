import sys
input = sys.stdin.readline

n = int(input())
lst = []
l = []

for _ in range(n):
    a, b= map(int,input().split())
    lst.append((a,b))
lst = sorted(lst, key = lambda x: (x[0], x[1]), reverse = True)
print(lst)
for i in lst:
    rank = 1
    for j in lst:
        if i[0] < j[0] and i[1] < j[1]: 
            rank +=1
    l.append(rank)

print(' '.join(map(str, l)))