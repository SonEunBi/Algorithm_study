import sys
input = sys.stdin.readline

num = int(input())
a = oct(num)[2:]
b = hex(num)[2:]
print(a, b.upper())