import sys
input = sys.stdin.readline

n = int(input())
print(bin(n).count('1'))