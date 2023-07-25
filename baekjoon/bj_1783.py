import sys
input = sys.stdin.readline

n = int(input())
region =  list(map(int, input().split()))
region = sorted(region)

ctr = int(input())
def finder(region):
    arr[0] = region[0]
    for i in range(1, n):
        tmp=[]
        arr.append(region[i])
        for j in range(i+1, n):
            tmp.append(region[j])  
            
        print(arr, tmp)  
        
        if arr[-1] < sum(tmp)//len(tmp):
            continue
        else:
            print(tmp, sum(tmp)//len(tmp))
            return sum(tmp)//len(tmp)
        
        
if sum(region) > ctr:
    arr=[]
    print(finder(region))
else:
    print(max(region))