def solution(a, b):
    answer = 0
    c = min(a, b)
    d = max(a, b)
    for i in range(c, d + 1):
        answer += i
    
    return answer