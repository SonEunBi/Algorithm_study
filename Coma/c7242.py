import sys
input = sys.stdin.readline
import time

start = time.time()
n = int(input())
word = []
word = [input().strip() for _ in range(n)]

#절반 쪼개서 단어 하나하나 분석하는 함수
def ispel(word):
    for i in range(len(word)//2):
        if word[i] != word[len(word)-1-i]:
            return False
    return True

#wl 안에는 숫자가 들어감
def dfs(wl, now):
    global n
    global res
    print(wl)
    if now == n:
        tmp =''
        for i in wl:
            tmp += word[i]
            #words의 i번째 있는 단어를 tmp에 합침
            if ispel(tmp):
                print('YES')
                print("time :", time.time() - start)
                exit(1)
            return
        
    for i in range(n):
        if i not in wl: #아직 다 검사 안했을 때
            store = wl.copy()
            store.append(i)
            dfs(store, now+1) #리스트를 갱신
             
dfs([], 0)

print('NO')
print("time :", time.time() - start)
