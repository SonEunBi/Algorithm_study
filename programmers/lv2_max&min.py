def solution(s):
    answer =''
    answer = list(map(int, s.split(' '))) #문자열을 숫자로 바꾸고
    answer = str(min(answer)) + " " + str(max(answer)) #숫자에서 최소 최대 구한 후 다시 answer형식인 문자열로 바꿔서 출력

    return answer