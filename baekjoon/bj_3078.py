import sys
input = sys.stdin.readline

n, k = map(int, input().split())
window = {i:0 for i in range(2,21)} #2는 몇개, 3은 몇 개, 4는 몇 개.. 이름 길이별로 개수 세서 저장함
student=[0]*n
ans =0                     
#덱 초기화

    
for i in range(n):
    f = str(input().rstrip())
    student[i] = len(f)
    if i > k: #윈도우 이동 시
        window[student[i-k-1]] -= 1
    ans += window[len(f)] # 먼저 +1을 해주면 안되는 이유는 문제 요구하는 것은 2인 이상의 쌍이기 때문
    #해당 len(f)는 현재 기준으로 두고 있는 학생을 의미함, 현재 학생의 길이가 window 안에 몇 개 있는지를 ans에 저장함(아직 +1을 안해줬으니까 현재 학생을 제외한 개수)
    window[len(f)] +=1
    
print(ans)
    
    
# while left <= right:
    
# for i in range(k):
#     if cls[i] == 
# for i in range(k, n):
    