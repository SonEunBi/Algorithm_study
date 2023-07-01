import sys
input = sys.stdin.readline

selfnum= []
notself =set()
def selfmake(num):
    num = num + sum(map(int, str(num)))
    return num

for i in range(1, 10001):
    notself.add(selfmake(i))

for i in range(1, 10001):
    if i not in notself:
        print(i)