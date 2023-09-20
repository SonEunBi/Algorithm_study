import sys
input = sys.stdin.readline
import math

n = int(input())
atd =list(map(int, input().split()))
b, c = map(int, input().split())
#총 감독관 - b명 , 부감독관 - c명 관리
#무조건 b는 ㅇㅋ
ans =n #n은 최솟값
for i in atd:
    ans += max(math.ceil((i-b)/c),0)
print(ans)


