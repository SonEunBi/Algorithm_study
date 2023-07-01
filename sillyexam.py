rows = 10
cols = 5
arr = [[j for j in range(cols)] for i in range(rows)]
print(arr)

for i in range(cols):
    arr[i] = list(map(int, input().split()))
    
arr = [list(map(int, input().split())) for _ in range(cols)]