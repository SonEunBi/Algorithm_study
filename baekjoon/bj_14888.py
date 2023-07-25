import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
cal = list(map(int, input().split())) #덧뺄곱나

oper = []
#연산자 idx 별로 구분해서 다시 저장
for idx, value in enumerate(cal):
    for _ in range(value):
        oper.append(idx)

oper = list(set(permutations(oper)))


ans=[]

for op in oper:
    res = nums[0]
    for num, o in zip(nums[1:], op):
        if o == 0:
            res += num
        elif o== 1:
            res -= num
        elif o ==2:
            res *= num
        else:
            if res <0:
                res = abs(res)
                res = -(res//num)
            else:
                res = res//num
    ans.append(res)
    
print(max(ans))
print(min(ans))