import sys
input = sys.stdin.readline

n, m = map(int, input().split())
viewer = [0] + list(map(int, input().split()))

if max(viewer) == 0:
    print('SAD')
else:
    window = sum(viewer[:m])
    answer = window
    cnt =1
    for i in range(m, n+1):
        window += viewer[i] - viewer[i-m]
        if window > answer:
            answer = window
            cnt =1
        elif window == answer:
            cnt +=1

    print(answer)
    print(cnt)
    