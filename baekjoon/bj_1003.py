import sys
input = sys.stdin.readline

n, m = map(int, input())
lcm = []
now =0
nums = [0] + list(map(int, input()))
for i in range(1, n+1):
    now = nums[i]
    