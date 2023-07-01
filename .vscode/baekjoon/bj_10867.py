import sys
read = sys.stdin.readline

n = int(read().strip())
lst = map(int, read().split())
s = sorted(list(set(lst)))

for i in s:
    print(i, end = ' ')