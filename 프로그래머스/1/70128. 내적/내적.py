def solution(a, b):
    answer = 0
    for i, j in list(zip(a, b)):
        answer += i * j
    return answer