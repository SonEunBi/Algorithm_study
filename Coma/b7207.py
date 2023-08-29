import sys 

n = int(input())
data = [[1 for _ in range(i)] for i in range(1, n+1)]

for i in range(3, n+1) :
  for j in range(1, i) :
    data[i][j] = data[i-1][j] +data[i-1][j-1]+ data[i-2][j]

for i in range(n):
    print(*data[i])