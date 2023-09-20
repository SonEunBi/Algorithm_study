def find(parent, node):
    if node == parent[node]:
        return parent[node]
    else:
        parent[node] = find(parent, parent[node])
    return parent[node]

def merge(parent, rank, u, v):
    rootU = find(parent, u)
    rootV = find(parent, v)

    if rootU != rootV:
        if rank[rootU] > rank[rootV]:
            parent[rootV] = rootU
        else:
            parent[rootU] = rootV
            if rank[rootU] == rank[rootV]:
                rank[rootV] += 1
res = 0
def calculate(n, m, taxi):
    global res
    for a, b, c in taxi:
        if find(parent, a - 1) != find(parent, b - 1):
            merge(parent, rank, a - 1, b - 1)
            res += c
    return res

n, m = map(int, input().split())
parent = [i for i in range(n)]
rank = [0]*n
taxi = []
for _ in range(m):
    a, b, c = map(int, input().split())
    taxi.append((a, b, c))

taxi.sort(key=lambda x: x[2])  
result = calculate(n, m, taxi)
print(result)