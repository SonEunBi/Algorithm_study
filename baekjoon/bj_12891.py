import sys
input = sys.stdin.readline

s, p = map(int, input().split())
dna = str(input().rstrip())
word2 = list(map(int, input().split()))
comp = {'A':0, 'C':0, 'G':0, 'T':0}
tmp = dna[:p]
cnt= 0
for i in tmp:
    comp[i] +=1
if comp['A'] >= word2[0] and comp['C'] >= word2[1] and comp['G'] >= word2[2] and comp['T'] >= word2[3]:
    cnt+=1

for i in range(s-p):
    comp[dna[i]] -=1
    comp[dna[i+p]] +=1
    if comp['A'] >= word2[0] and comp['C'] >= word2[1] and comp['G'] >= word2[2] and comp['T'] >= word2[3]:
        cnt+=1
print(cnt)