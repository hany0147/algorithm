from itertools import combinations

def solution(number):
    lst = list(combinations(number, 3))
    answer = 0
    for i in lst:
        if sum(i) == 0:
            answer += 1
    return answer