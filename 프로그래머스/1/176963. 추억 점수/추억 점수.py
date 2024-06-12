def solution(name, yearning, photo):
    answer = []
    
    
    for p in photo:
        tmp = 0
        for i in p:
            if i in name:
                tmp += yearning[name.index(i)]
        answer.append(tmp)
    return answer