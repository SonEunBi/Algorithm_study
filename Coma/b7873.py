import sys, re

input = sys.stdin.readline

s =input()

def isPhone(text):
    if len(text) != 13:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
        if text[3] != '-':
            return False
        for i in range(4, 8):
            if not text[i].isdecimal():
                return False
        if text[8] != '-':
            return False
        for i in range(9, 13):
            if not text[i].isdecimal():
                return False
    return True

pattern = r"010-\d{4}-\d{4}"
answer = re.findall(pattern, s)
if isPhone(s):
    print('valid')
else:
    print('invalid')