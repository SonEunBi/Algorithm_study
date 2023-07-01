import sys
input = sys.stdin.readline

ans =0
dial = ['ABC', 'DEF','GHI', 'JKL', 'MNO','PQRS', 'TUV', 'WXYZ']
word = input().strip()
for alphabet in dial:
    for spelling in alphabet:
        for i in word:
            if i == spelling:
                ans += dial.index(alphabet) + 3
print(ans)