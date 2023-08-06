import sys
input = sys.stdin.readline

sensor = int(input())
cnt = int(input())
lo = list(map(int, input().split()))
lo.sort()
dif = []

for i in range(1, sensor):
    dif.append(lo[i]- lo[i-1])
dif.sort()

print(sum(dif[:sensor-cnt]))