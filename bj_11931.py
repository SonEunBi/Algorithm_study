import sys
read = sys.stdin.readline
lst = []
n = int(read().rstrip())
for i in range(n):
    lst.append(int(read().rstrip()))

lst.sort(reverse=True)
for i in range(n):
    print(lst[i])