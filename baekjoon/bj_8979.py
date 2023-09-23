import sys
input = sys.stdin.readline

n, k = map(int, input().split())
rank = []
for i in range(n):
    nat, m1, m2, m3 = map(int, input().split())
    rank.append((nat,m1,m2,m3))

rank.sort(key = lambda x: (x[1], x[2], x[3]), reverse=True)

idx = [rank[i][0] for i in range(n)].index(k)

for i in range(n):
    if rank[idx][1:] == rank[i][1:]:
        print(i+1)
        break

    