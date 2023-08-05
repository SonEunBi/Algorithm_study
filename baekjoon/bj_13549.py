import sys
from collections import deque

def bfs(n, k):
    visited = [False] * 100001
    visited[n] = True
    queue = deque()
    queue.append((N, 0))

    while queue:
        pos, cost = queue.popleft()

        if pos == k:
            return cost

        if pos * 2 >= 0 and pos * 2 <= 100000 and not visited[pos * 2]:
            visited[pos * 2] = True
            queue.append((pos * 2, cost))
        if pos - 1 >= 0 and pos - 1 <= 100000 and not visited[pos - 1]:
            visited[pos - 1] = True
            queue.append((pos - 1, cost + 1))
        if pos + 1 >= 0 and pos + 1 <= 100000 and not visited[pos + 1]:
            visited[pos + 1] = True
            queue.append((pos + 1, cost + 1))

N, K = map(int, sys.stdin.readline().split())
print(bfs(N, K))