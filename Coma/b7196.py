import sys
input = sys.stdin.readline

n = input()
cnt =1
# hour = [str(i) for i in range(0, 24)]
# minute = [str(i) for i in range(0, 60)]
# for i in minute:
#     for j in i:
#         if j == n:
#             cnt +=1
# cnt = cnt*2
# for i in hour:
#     for j in i:
#         if j == n:
#             cnt +=1

# print(cnt*59*59)

sumSec=0    # 초의 총합을 저장할 변수
for hour in range(24) :     # 시간
    for minute in range(60) :   #분
        if n in str(hour) or n in str(minute) : # 시간이나 분에 3이 들어가면
            sumSec += 60            # 60초씩 더함
print(sumSec)