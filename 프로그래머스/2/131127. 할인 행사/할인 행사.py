from copy import deepcopy

def solution(want, number, discount):
    answer = 0

    for i in range(len(discount)):
        tmp = deepcopy(number)
        if i + 10 > len(discount):
            break
        for j in range(i, i + 10):
            if discount[j] in want and tmp[want.index(discount[j])] > 0:
                tmp[want.index(discount[j])] -= 1

        if all(val == 0 for val in tmp):
            answer += 1

    return answer
