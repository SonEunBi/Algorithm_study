import math
t =int(input())
grade =[]
for i in range(t):
    ans, cnt, avgg=0,0, 0
    grade.clear()
    grade = list(map(int, input().split()))
    avgg = sum(grade[1:])/grade[0]
    for j in range(grade[0]):
        if grade[j] > avgg:
            cnt+=1
    ans = cnt/ grade[0] * 100
    print('%.3f' %ans, '%')