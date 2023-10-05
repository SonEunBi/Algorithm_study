def solution(genres, plays):
    answer = []
    mlist = {}
    total_score={}
    
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre in mlist:
            mlist[genre].append((idx, play))
            total_score[genre] += play
        else:
            mlist[genre] = [(idx, play)]
            total_score[genre] = play
    
    mlist = sorted(mlist.items(), key=lambda x: total_score[x[0]], reverse=True) 
    
    for genre, info in mlist: #장르, 노래정보
        for idx, play in sorted(info, key= lambda x: x[1], reverse=True)[:2]:
            answer.append(idx)

    return answer