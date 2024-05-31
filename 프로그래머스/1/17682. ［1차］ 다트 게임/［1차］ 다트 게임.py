def solution(dartResult):
    bonus = {
        'S': 1,
        'D': 2,
        'T': 3
    }
    
    score = []
    tmp = ""
    for i in dartResult:
        if i.isdigit():
            tmp += i
        elif i.isalpha():
            score.append(int(tmp) ** bonus[i])
            tmp = ""
            
        if i == "*":
            score[-1] *= 2
            if len(score) >= 2:
                score[-2] *= 2
        if i == "#":
            score[-1] *= -1

    return sum(score)