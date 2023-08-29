import sys

r = int(input())
PI = 3.14
ans = r*r*PI
if r <50:
    print("{:g}".format(r*r*PI))
else:
    print(format(ans, '.2f'))