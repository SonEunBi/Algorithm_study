def solution(numbers, target):
    cnt =0
    arr =[0]
    for i in numbers:
        tmp = []
        for j in arr:
            tmp.append(j + i)
            tmp.append(j - i)
        arr = tmp
    for i in arr:
        if i == target:
            cnt+=1
    return cnt