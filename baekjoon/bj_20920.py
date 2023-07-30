import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memory = {}
for _ in range(n):
    word = input().rstrip()
    if len(word) < m :#길이 체크
        continue
    else:
        if word in memory:
            memory[word] +=1
        else:
            memory[word] =1

memory = sorted(memory.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))

for key in memory:
    print(key[0])