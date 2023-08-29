import sys
input = sys.stdin.readline

n = int(input())
arr = []
maxDP = arr

for _ in range(n - 1):
    arr = list(map(int, input().split()))
    maxDP = [arr[1] + max(maxDP), arr[2] + max(maxDP[1], maxDP[2])]

print(maxDP)