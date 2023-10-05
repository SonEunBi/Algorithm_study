def solution(name, yearning, photo):
    answer = []
    name_dict= dict(zip(name, yearning))
    
    for col in photo:
        result =0
        
        for row in col:
            result += name_dict.get(row,0)
            # get을 쓸 때 row에 값이 없을 때를 대비하여 뒤에 0을 써줘야 함
        answer.append(result)
    return answer