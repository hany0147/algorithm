def solution(k, score):
    # honor = sorted(score[:k])
    # print(honor)
    answer = []
    honor = []
    for i in score[:k]:
        honor.append(i)
        answer.append(min(honor))
    honor.sort(reverse=True)
    for i in score[k:]:
        if i > honor[-1]:
            honor.pop()
            honor.append(i)
            honor.sort(reverse=True)
        answer.append(min(honor))
            
    return answer