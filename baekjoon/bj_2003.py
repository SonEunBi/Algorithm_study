n, m = map(int, input().split())
num = list(map(int, input().split()))

cnt =0
left, right =0,1
while right <= n and left <= right:
    prefix_sum = sum(num[left:right])
    if prefix_sum == m:
        cnt +=1
        right +=1
    elif prefix_sum < m:
        right +=1
    elif prefix_sum > m:
        left +=1 
print(cnt)