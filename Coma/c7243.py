from itertools import combinations_with_replacement

n, k = map(int, input().split())
alpha = input().split()

combi = list(combinations_with_replacement(alpha,  k))

for i in combi:
    print('\n'.join(i))