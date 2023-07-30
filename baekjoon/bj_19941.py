import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = list(input().rstrip())
cnt =0
for i in range(n):
    if s[i] == 'P':
        for j in range(i-k, i+k+1):
            if -1 < j < n and  s[j] == 'H':
                s[j] = '0'
                cnt +=1
                break
print(cnt)