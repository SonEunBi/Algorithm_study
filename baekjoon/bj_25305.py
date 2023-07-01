import sys
read = sys.stdin.readline

n, k = map(int, read().split())
num = list(map(int, read().split()))

num.sort(reverse= True)
print(num[k-1])