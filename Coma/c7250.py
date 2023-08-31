import sys
input = sys.stdin.readline

s = input()
dele = s.split('F')
print(s)
cnt =0
for i in range(len(s)):
    if dele[0] == '' or dele[-1] =='':
    