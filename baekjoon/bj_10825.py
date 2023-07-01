import sys
read = sys.stdin.readline

n = int(read().strip())
student = []
ans =[]
for i in range(n):
    student.append(list(read().split()))
ans = student.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in range(n):
    print(student[i][0])