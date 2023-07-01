import sys
read = sys.stdin.readline

student =[0]*(30)
arr = []
for i in range(28):
    num = int(read().strip())
    student[num-1] = 1
    
for i in range(30):
    if student[i] == 0:
        arr.append(i+1)
arr.sort()
print(arr[0])
print(arr[1])
