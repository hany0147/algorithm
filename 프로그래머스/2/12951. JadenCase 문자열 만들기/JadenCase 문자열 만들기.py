def solution(s):
    answer = ''
    flag = True
    for idx, item in enumerate(s):
        if item == ' ':
            flag = True
            answer += item
        else:
            if flag:
                answer += item.upper()
                flag = False
            elif not flag:
                answer += item.lower()
    return answer