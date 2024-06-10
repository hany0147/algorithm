def solution(food):
    tmp = [1]
    answer = ''
    for i in range(1, len(food)):
        if food[i] % 2 != 0:
            tmp.append(food[i] - 1)
        else:
            tmp.append(food[i])
    
    for idx, num in enumerate(tmp):
        if idx == 0:
            continue
        if num == 0:
            continue
        answer += str(idx) * (num // 2)
    
    reverse_answer = answer[::-1];
    answer = answer + "0" + reverse_answer
    
    return answer