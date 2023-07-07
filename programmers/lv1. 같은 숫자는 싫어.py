def solution(arr):
    answer = []
    s = set()
    q = [arr[0]]
    j=0
    for i in range(1, len(arr)):
        if q[j] == arr[i]:
            continue
        else:
            q.append(arr[i])
            j+=1
            
    
    return q