import sys
read = sys.stdin.readline

n, s = map(int, read().split())

l_s =set()
s_s = set()

for i in range(n):
    l_s.add(read().strip())

for j in range(s):
    s_s.add(read().strip())

s = sorted(list(l_s & s_s))
print(len(s))
for i in s:
    print(i)
    