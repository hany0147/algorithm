def solution(k, m, score):
    score.sort(reverse = True)
    
    res = []    
    
    tmp = []
    cnt = 0

    for i in score:
        tmp.append(i)
        cnt += 1
        if cnt == m:
            res.append(tmp)
            tmp = []
            cnt = 0
    
    answer = 0
    
    for i in res:
        answer += min(i) * m
    
    return answer