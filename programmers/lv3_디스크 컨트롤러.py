import heapq

def solution(jobs):
    answer = 0
    l = len(jobs)
    now = 0
    last = -1
    pq = []
    i = 0

    while i < l:
        # 현재 시간보다 이전에 요청된 작업을 모두 큐에 추가
        for job in jobs:
            if last < job[0] <= now:
                answer += (now - job[0])
                heapq.heappush(pq, job[1])

        if pq:
            answer += (len(pq) * pq[0])
            last = now
            now += heapq.heappop(pq)
            i += 1  
        else:
            now += 1

    return int(answer // l)
