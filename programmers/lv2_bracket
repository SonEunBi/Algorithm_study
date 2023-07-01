def solution(s):
    answer = True
    stack =[]
    for i in s:
        if i == "(":
            stack.append(i)
        else: #')'이거면 무조건 스택에 들어갈 문자 없음
            if stack == []:
                return False
            else:
                stack.pop()
            
    return len(stack)==0