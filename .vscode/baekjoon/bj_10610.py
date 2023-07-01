import sys
read= sys.stdin.readline

n = read().strip()
ans =0

if '0' in n:
    for i in range(len(n)):
        ans += int(n[i])
        if ans %3 == 0:
            n = list(map(int, n))
            n.sort(reverse=True)
            n = list(map(str, n))
            print(''.join(n))
else:
    print('-1')