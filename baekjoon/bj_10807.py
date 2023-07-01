import sys
read = sys.stdin.readline

n = int(read())
num = list(map(int, read().split()))

v = int(read())
print(num.count(v))