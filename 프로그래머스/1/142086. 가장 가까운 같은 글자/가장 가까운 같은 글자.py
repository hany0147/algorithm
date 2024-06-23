def solution(s):
    lst = []
    answer = []
    for i in s:
        if i not in lst:
            answer.append(-1)
        else:
            cnt = 0
            for j in lst[::-1]:
                cnt += 1
                if i == j:
                    answer.append(cnt)
                    break
        lst.append(i)
                    
            
    return answer