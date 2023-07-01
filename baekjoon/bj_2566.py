import sys
read= sys.stdin.readline

board =[]
maxn, col, row =0,0,0

for _ in range(9):
    board.append(list(map(int, read().split())))

for i in range(9):
    for j in range(9):
        if maxn <= board[i][j]:
            maxn = board[i][j]
            row = i+1
            col = j+1
            
print(maxn)
print(row, col)
        
        
        