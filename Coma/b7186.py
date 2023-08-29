import sys
input = sys.stdin.readline

n = int(input())
new_l =[]
l = set()
for i in range(n):
    a= input().rstrip('\n')
    l.add((a, len(a)))
new_l = sorted(l, key= lambda x : (x[1] , x[0]))
for i in new_l:
    print(i[0])