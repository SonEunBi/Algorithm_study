import sys
read = sys.stdin.readline

n = int(read().strip())

board = [[0]*101 for _ in range(101)]

for i in range(n):
    x, y = map(int, read().split())
    
    for row in range(x, x+10):
        for col in range(y, y+10):
            board[row][col] =1
cnt =0 
for i in range(100):
    for j in range(100):
        if board[i][j] == 1:
            cnt +=1
for i in board:
    cnt += i.count(1)
    
print(cnt)

'''

'''